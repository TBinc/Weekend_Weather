from typing import Optional, Union
from weather_api import get_dummy_data, get_printable_forecast, get_weather_data
from diagram.utils import _create_diagram


def empty_diagram(path: str = './') -> None:
    """
    Creates an empty diagram at the specified path.

    Args:
        path (str, optional): Path where the diagram is to be saved. Defaults to './'.
    """
    _create_diagram(path=path)


def filled_diagram(zip_code: Union[str, int], aggregated: bool = False, data: Optional[dict] = None,
                   path: str = './') -> None:
    """
    Creates a filled diagram with weather data at the specified path.

    Args:
        zip_code (Union[str, int]): ZIP code for which the weather data is to be fetched.
        aggregated (bool, optional): Whether the weather data should be aggregated. Defaults to False.
        data (dict, optional): Weather data. If None, fetches the data from the weather API. Defaults to None.
        path (str, optional): Path where the diagram is to be saved. Defaults to './'.
    """
    # Fetch data from weather API if not provided
    if data is None:
        data = get_weather_data(zip_code)

    # Generate printable forecast from the data
    res = get_printable_forecast(data, aggregated=aggregated, sample=True)

    # Create diagram with the printable forecast
    _create_diagram(zip_code=zip_code, aggregated=aggregated, data_ex=res, path=path)
