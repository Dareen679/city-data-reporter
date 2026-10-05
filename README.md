# City Data Reporter

## About the Project

City Data Reporter is a Python command-line program that retrieves current weather information for a city using the OpenWeatherMap API.

The user enters a city name, and the program displays the city's country, current temperature in Celsius, humidity, and weather description. The program also saves the information to a CSV file and reads the saved data back from the file.

## Features

- Accepts a city name from the user
- Prevents empty city names from being submitted
- Retrieves live weather data from OpenWeatherMap
- Handles invalid city names and API errors
- Displays temperature, humidity, country, and weather description
- Saves weather information to `city_data.csv`
- Reads saved city information from the CSV file
- Reports the number of cities saved in the file

## Libraries Used

This project uses the following Python libraries:

- `requests` - sends the GET request to the OpenWeatherMap API
- `json` - parses the JSON response from the API
- `csv` - writes and reads weather information from the CSV file
- `os` - accesses the API key stored as an environment variable

## Getting an OpenWeatherMap API Key

1. Go to https://openweathermap.org/
2. Create a free account or sign in.
3. Open the API Keys section of your account.
4. Copy your API key.
5. Keep the API key private and do not place it directly inside `reporter.py`.

## Setup

Make sure Python is installed.

Install the `requests` library by running:

```bash
python3 -m pip install requests
export OPENWEATHER_API_KEY="YOUR_API_KEY_HERE"
```
## Running the Program

Run the program from the terminal with:

    python3 reporter.py

The program will ask you to enter a city name.

Example:

    Enter a city name: Minneapolis

The program will display the current weather information and save it to `city_data.csv`.

## CSV Output

The CSV file contains these columns:

- City
- Country
- Temperature (C)
- Humidity (%)
- Description

The program also reads the CSV file and displays the number of saved cities along with each city's temperature.

## Screencast

Screencast video: https://www.loom.com/share/0c7426698b2e49e9856d820b16e97030