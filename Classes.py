class Forecast():
    
    def __init__(self, city, country, timestamps_list):
        self.city = city
        self.country = country
        self.timestamps_list = timestamps_list

        temperatures = []
        for ts in timestamps_list:
            temperatures.append(ts.temperature)
        
        self.temp_min = min(temperatures)
        self.temp_max = max(temperatures)


class Timestamps():

    def __init__(self, datetime, temperature):
        self.datetime = datetime
        self.temperature = temperature