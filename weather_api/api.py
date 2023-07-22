from typing import  Dict, Any
from datetime import datetime

from weather_api.utils import _to_f


def get_printable_forecast(
    forecast: Dict[datetime, Dict[datetime, Dict[str, Any]]],
    aggregated: bool = False,
    sample: bool = False,
) -> str:
    """
    Function to create a printable string from a weather forecast.

    Args:
        forecast (dict): A dictionary containing datetime and weather information
        aggregated (bool): If true, it returns aggregated weather data. Defaults to False
        sample (bool): If true, only sample data will be returned. Defaults to False

    Returns:
        str: A string of printable forecast data
    """
    res = ""
    new_line = "\n"

    if sample:
        new_line += new_line
    for date, times in forecast.items():
        res += f"\nDate: {date}"

        # Initialize variables for aggregated calculations
        temp_sum = 0
        feels_like_sum = 0
        temp_min = float("inf")
        temp_max = float("-inf")
        count = 0

        for time, weather in times.items():
            temp_f = _to_f(weather["temp"])
            feels_like_f = _to_f(weather["feels_like"])
            temp_min_f = _to_f(weather["temp_min"])
            temp_max_f = _to_f(weather["temp_max"])

            # Update aggregated calculations
            temp_sum += temp_f
            feels_like_sum += feels_like_f
            temp_min = min(temp_min, temp_min_f)
            temp_max = max(temp_max, temp_max_f)
            count += 1

            if not aggregated:
                res += new_line + f"\nTime: {time}"
                res += new_line + f"Temperature: {temp_f:.2f} °F"
                res += new_line + f"Feels Like: {feels_like_f:.2f} °F"
                res += new_line + f"Min Temperature: {temp_min_f:.2f} °F"
                res += new_line + f"Max Temperature: {temp_max_f:.2f} °F"
                res += new_line + f"Pressure: {weather['pressure']} hPa"
                res += new_line + f"Humidity: {weather['humidity']}%"
                res += new_line + "\n-------------------------"

                if sample:
                    break
        if aggregated:
            res += new_line + f"Average Temperature: {temp_sum / count:.2f} °F"
            res += new_line + f"Average Feels Like: {feels_like_sum / count:.2f} °F"
            res += new_line + f"Min Temperature: {temp_min:.2f} °F"
            res += new_line + f"Max Temperature: {temp_max:.2f} °F"
            res += new_line + "\n-------------------------"
    return res
