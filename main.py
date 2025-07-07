import requests
import json
import click
from loguru import logger
import Classes

logger.add("main.log", rotation="1 MB", retention="7 days", level="INFO")


#Récupération de la ville et du pays passé en CLI au démarrage du script
@click.command()
@click.argument('city')
@click.argument('country')
def main(city, country):
    logger.info(f"Tentative de récupération de prévisions météo pour {city} {country}")

    api_key = ""

    #Récupération de la clé API dans config.json
    try:
        logger.info("Lecture du fichier config.json")
        with open("config.json", "r") as config_file:
            config_data = json.load(config_file)
            api_key = config_data["api_key"]
            logger.success("Clé API chargée correctement")
    except Exception as e:
        logger.error(f"Impossible de lire le fichier config.json : {e}")

    #Paramétrage de l'appel API avec les données de l'utilisateur
    api_endpoint = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country}&appid={api_key}&limit=5&units=metric"

    logger.debug(f"Endpoint API appelé : {api_endpoint}")
    response = requests.get(api_endpoint) #Appel sur l'URL avec Requests

    logger.info("Démarrage de la requête API")
    if response.status_code == 200:
        logger.success("La requête a abouti avec succès")
        #Conversion du résultat au format json interprêtable par python
        data = response.json()

        timestamps_list = [] #Liste contenant les différentes entrées à intervale de 3 heures

        #Parcours des résultats de l'API en stockant les données importantes dans des variables
        for item in data['list']:
            datetime = item['dt_txt'] #Date et heure de l'enregistrement
            temp = item['main']['temp'] #Température

            #Création d'un nouvel objet Timestamps contenant les infos et stockage dans la liste
            ts = Classes.Timestamps(datetime, temp)
            timestamps_list.append(ts)

        country = data["city"]["country"] #Récupération du code pays (au cas ou l'utilisateur a entré le nom du pays en entier)
        city = data["city"]["name"] #Récupération du nom de la ville (au cas ou l'utilisateur l'a mal orthographié)
        forecast = Classes.Forecast(city, country, timestamps_list) #Création d'un objet Forecast contenant les infos et la liste de ts

        #Regroupement des entrées par date -> un dictionnaire qui a pour clé la date et pour valeur une liste de toutes les températures
        daily_data = {}
        for ts in timestamps_list:
            date = ts.datetime.split(" ")[0] #Séparation de la date et de l'heure en sauvegardant que la date
            if date not in daily_data: #Si la date n'existe pas dans le dico, on l'ajoute
                daily_data[date] = []
            daily_data[date].append(ts.temperature) #Ajouter la température à la liste correspondante

        #Génération du résultat json forecast_details
        forecast_details = []
        for date, temps in daily_data.items(): #Parcours du dico
            measure_count = len(temps) #Compter le nombre de températures utilisés pour calculer la moyenne
            avg_temp = sum(temps) / measure_count #Calculer la moyenne

            #N'ajouter l'entrée que s'il n'y en a pas déjà 5
            if len(forecast_details) < 5:
                forecast_details.append({
                    "date": date,
                    "temp": round(avg_temp, 2),
                    "measure_count": measure_count
                })

        #Générer le résultat json final avec toutes les informations
        result = {
            "forecast_location": f"{city}({country})",
            "forecast_min_temp": forecast.temp_min, #Calculé automatiquement lors de l'initialisation de l'objet
            "forecast_max_temp": forecast.temp_max, #Calculé automatiquement lors de l'initialisation de l'objet
            "forecast_details": forecast_details 
        }

        logger.info("Tentative d'enregistrement des données dans forecast.json")
        try:
            #Ecriture du résultat dans le fichier forecast.json
            with open("forecast.json", "w") as json_file:
                json.dump(result, json_file, indent=4)
            logger.success("Les données météo ont été enregistrées dans forecast.json")
            print("Les données de prévision ont été enregistrées dans le fichier json")
        except Exception as e:
            logger.error(f"Erreur lors de l'enregistrement des données : {e}")
            print("Erreur lors de l'enregistrement des données.")
    else:
        data = response.json()
        logger.error(f"Erreur de récupération des données : {data['cod']} - {data['message']}")
        print(f"Erreur {data['cod']} - {data['message']}")


main()
