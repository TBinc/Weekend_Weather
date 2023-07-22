from weather_api import get_printable_forecast, get_weather_data
from datetime import datetime


def test_get_printable_forecast():
    # Create a sample forecast data for testing
    forecast_data = {
        datetime(2023, 7, 22): {
            datetime(2023, 7, 22, 9, 0): {"temp": 300, "feels_like": 295, "temp_min": 298, "temp_max": 302, "pressure": 1015, "humidity": 60},
            datetime(2023, 7, 22, 12, 0): {"temp": 302, "feels_like": 298, "temp_min": 300, "temp_max": 305, "pressure": 1014, "humidity": 58},
        },
        datetime(2023, 7, 23): {
            datetime(2023, 7, 23, 9, 0): {"temp": 298, "feels_like": 294, "temp_min": 296, "temp_max": 301, "pressure": 1016, "humidity": 62},
            datetime(2023, 7, 23, 12, 0): {"temp": 300, "feels_like": 296, "temp_min": 297, "temp_max": 303, "pressure": 1015, "humidity": 63},
        }
    }

    # Call the function with the sample forecast data
    printable_forecast = get_printable_forecast(forecast_data)

    # Check if the returned value is a non-zero length string
    assert isinstance(printable_forecast, str)
    assert len(printable_forecast) > 0


def test_get_weather_data():
    # Replace this with a valid ZIP code for your location
    valid_zip_code = "32216"

    # Call the function with a valid ZIP code
    forecast_data = get_weather_data(valid_zip_code)

    # Check if the returned value is a non-empty dictionary
    assert isinstance(forecast_data, dict)
    assert len(forecast_data) > 0
