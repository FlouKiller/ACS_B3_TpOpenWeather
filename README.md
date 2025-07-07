# OpenWeather Forecast Application

A Python command-line application that fetches weather forecast data from the OpenWeatherMap API and processes it to provide 5-day weather predictions for any city.

## 📋 Features

- **Command-line interface** for easy city and country input
- **5-day weather forecast** with temperature predictions
- **Automatic data processing** with daily temperature averages
- **JSON output** for easy data integration
- **Comprehensive logging** with rotation and retention policies
- **Error handling** for API failures and invalid inputs

## 🛠️ Prerequisites

- Python 3.7+
- OpenWeatherMap API key (free registration at [openweathermap.org](https://openweathermap.org/api))

## 📦 Installation

1. **Clone or download** this repository to your local machine

2. **Install dependencies** using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API key** in `config.json`:
   ```json
   {
       "api_key": "your_openweathermap_api_key_here"
   }
   ```

## 🚀 Usage

Run the application from the command line with the following syntax:

```bash
python main.py <city> <country>
```

### Examples

```bash
# Get forecast for Paris, France
python main.py Paris FR

# Get forecast for New York, United States
python main.py "New York" US

# Get forecast for Tokyo, Japan
python main.py Tokyo JP
```

### Parameters

- **city**: Name of the city (use quotes for multi-word cities)
- **country**: ISO 3166 country code (e.g., FR, US, JP, DE)

## 📁 Project Structure

```
ACS_B3_TpOpenWeather/
├── main.py              # Main application entry point
├── Classes.py           # Data models (Forecast, Timestamps)
├── config.json          # API configuration (NOT COMMITTED)
├── requirements.txt     # Python dependencies
├── forecast.json        # Generated forecast output (created after first run)
├── main.log             # Application logs (created after first run)
└── README.md            # This file
```

## 📊 Output

The application generates a `forecast.json` file containing:

```json
{
    "forecast_location": "Paris(FR)",
    "forecast_min_temp": 15.2,
    "forecast_max_temp": 24.8,
    "forecast_details": [
        {
            "date": "2025-07-07",
            "temp": 20.5,
            "measure_count": 8
        },
        {
            "date": "2025-07-08",
            "temp": 22.1,
            "measure_count": 8
        }
        // ... up to 5 days
    ]
}
```

### Output Fields

- **forecast_location**: City and country code
- **forecast_min_temp**: Lowest temperature in the 5-day period
- **forecast_max_temp**: Highest temperature in the 5-day period
- **forecast_details**: Array of daily forecasts containing:
  - **date**: Date in YYYY-MM-DD format
  - **temp**: Average temperature for the day (°C)
  - **measure_count**: Number of measurements used for the average

## 🏗️ Architecture

### Classes

- **Forecast**: Represents weather forecast data for a location
  - Stores city, country, and timestamps
  - Automatically calculates min/max temperatures

- **Timestamps**: Represents individual weather measurements
  - Contains datetime and temperature data

### Dependencies

- **requests**: HTTP library for API calls
- **click**: Command-line interface framework
- **loguru**: Advanced logging with rotation
- **json**: Built-in JSON handling

## 📝 Logging

The application uses `loguru` for comprehensive logging:

- **Log file**: `main.log`
- **Rotation**: 1 MB file size limit
- **Retention**: 7 days
- **Level**: INFO and above

Log entries include:
- API request attempts
- Configuration loading
- Success/error messages
- Debug information for troubleshooting

## ⚠️ Error Handling

The application handles various error scenarios:

- **Invalid API key**: Returns authentication error
- **City not found**: Returns location not found error
- **Network issues**: Logs connection errors
- **Configuration errors**: Logs config file reading issues

## 🔧 Configuration

### API Key Setup

1. Register at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your free API key
3. Update `config.json` with your key:
   ```json
   {
       "api_key": "your_actual_api_key_here"
   }
   ```

### Customization

You can modify the following in `main.py`:
- Temperature units (currently set to metric/Celsius)
- Number of forecast days (currently 5)
- Log level and retention settings

## 🌡️ API Information

This application uses the OpenWeatherMap 5-day/3-hour forecast API:
- **Endpoint**: `api.openweathermap.org/data/2.5/forecast`
- **Data interval**: Every 3 hours
- **Forecast period**: 5 days
- **Temperature unit**: Celsius (metric)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is provided as-is for educational purposes. Please respect OpenWeatherMap's API terms of service.

## 🐛 Troubleshooting

### Common Issues

1. **"Invalid API key"**
   - Check your API key in `config.json`
   - Ensure the key is active (may take a few hours after registration)

2. **"City not found"**
   - Verify city name spelling
   - Use correct ISO country code
   - Try using English city names

3. **"Module not found"**
   - Install dependencies: `pip install -r requirements.txt`

4. **"Permission denied" (log file)**
   - Ensure write permissions in the project directory

### Support

Check the `main.log` file for detailed error information and debugging data.
