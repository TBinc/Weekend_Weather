import requests
import os
import getpass
from datetime import datetime
from collections import defaultdict
from weather_api.dummy import DUMMY_DATA
from typing import Dict, Any, Union


def get_api_key(api_key: str = None) -> str:
    """
    Function to retrieve the API key from environment variables or user input.
    If the API key is not found in the environment variables, it will prompt the user to input the key.

    Args:
        api_key (str): An optional string containing the API key

    Returns:
        str: The retrieved API key
    """
    api_key = api_key or os.environ.get("OPENWEATHER_API_KEY")

    if not api_key:
        print("API key not found.")
        api_key = getpass.getpass(prompt="Enter API key: ")
    os.environ["OPENWEATHER_API_KEY"] = api_key
    return api_key


def destroy_api_key() -> None:
    """
    Function to remove the API key from the environment variables.
    """
    if "OPENWEATHER_API_KEY" in os.environ:
        del os.environ["OPENWEATHER_API_KEY"]
    return


def _to_f(k: float) -> float:
    """
    Helper function to convert temperature from Kelvin to Fahrenheit.

    Args:
        k (float): Temperature in Kelvin

    Returns:
        float: Temperature in Fahrenheit
    """
    f = k * 9 / 5 - 459.67
    return f


def get_dummy_data(zip_code: str) -> Dict[datetime, Dict[datetime, Dict[str, Any]]]:
    """
    Function to return dummy weather data for a given zip code.

    Args:
        zip_code (str): The zip code for the desired weather data

    Returns:
        dict: A dictionary containing datetime and weather information
    """
    data = DUMMY_DATA
    if data["cod"] != "200":
        raise ValueError(data["message"])
    data = data.get("list")
    forecast = defaultdict(dict)

    for info in data:
        # Checks if the day is weekend
        info_date = datetime.fromtimestamp(info["dt"])
        if info_date.weekday() not in (5, 6):
            continue
        forecast[info_date.date()][info_date.time()] = info["main"]
    return forecast  # {'datetime': 'projection'}


def get_weather_data(zip_code: str) -> Dict[datetime, Dict[datetime, Dict[str, Any]]]:
    """
    Function to get weather data for a given zip code.

    Args:
        zip_code (str): The zip code for the desired weather data

    Returns:
        dict: A dictionary containing datetime and weather information
    """
    data = _get_forecast(zip_code)
    if data["cod"] != "200":
        raise ValueError(data["message"])
    data = data.get("list")
    forecast = defaultdict(dict)

    for info in data:
        # Checks if the day is weekend
        info_date = datetime.fromtimestamp(info["dt"])
        if info_date.weekday() not in (5, 6):
            continue
        forecast[info_date.date()][info_date.time()] = info["main"]

    # If there is nothing to show because it has been run on monday it will get data from disk to show workings
    if len(forecast) == 0:
        print('Data for next week unavailable, using stored data')
        forecast = get_dummy_data(zip_code)

    return forecast  # {'datetime': 'projection'}


def _get_forecast(zip_code: str) -> Dict[str, Union[str, int, list]]:
    """
    Function to send a GET request to the OpenWeather API and return the forecast data.

    Args:
        zip_code (str): The zip code for the desired weather data

    Returns:
        dict: A dictionary containing the returned data from the API
    """
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"zip": f"{zip_code},us", "appid": get_api_key()}
    response = requests.get(base_url, params=params)
    return response.json()
