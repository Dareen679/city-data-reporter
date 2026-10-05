import csv
import json
import os

import requests


def get_city_name():
    """Ask the user for a city name and make sure it is not empty."""
    while True:
        city = input("Enter a city name: ").strip()

        if city:
            return city

        print("City name cannot be empty. Please try again.")


def get_weather_data(city, api_key):
    """Get current weather data for a city from OpenWeatherMap."""
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 404:
            print("City not found. Please check the city name.")
            return None

        if response.status_code == 401:
            print("API key error. Please check your API key.")
            return None

        response.raise_for_status()

        data = json.loads(response.text)
        return data

    except requests.RequestException as error:
        print(f"An error occurred while connecting to the API: {error}")
        return None


def display_weather(data):
    """Display important weather information and return it as a dictionary."""
    city = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print("\n--- City Weather Report ---")
    print(f"City: {city}")
    print(f"Country: {country}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description.title()}")

    return {
        "City": city,
        "Country": country,
        "Temperature (C)": temperature,
        "Humidity (%)": humidity,
        "Description": description
    }


def save_to_csv(weather_info):
    """Save the city weather information to city_data.csv."""
    file_name = "city_data.csv"
    file_exists = os.path.exists(file_name)

    with open(file_name, "a", newline="", encoding="utf-8") as csv_file:
        fieldnames = [
            "City",
            "Country",
            "Temperature (C)",
            "Humidity (%)",
            "Description"
        ]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(weather_info)

    print("\nWeather data saved to city_data.csv.")


def read_city_data():
    """Read the CSV file and report saved cities and temperatures."""
    file_name = "city_data.csv"

    try:
        with open(file_name, "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            cities = list(reader)

        print(f"\nCities currently saved: {len(cities)}")

        for city in cities:
            print(f"{city['City']}: {city['Temperature (C)']}°C")

    except FileNotFoundError:
        print("No city_data.csv file has been created yet.")


def main():
    """Run the City Data Reporter program."""
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        print("OPENWEATHER_API_KEY is not set.")
        print("Please set your API key before running the program.")
        return

    city = get_city_name()
    weather_data = get_weather_data(city, api_key)

    if weather_data:
        weather_info = display_weather(weather_data)
        save_to_csv(weather_info)
        read_city_data()


if __name__ == "__main__":
    main()