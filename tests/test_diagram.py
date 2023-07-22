import os
from unittest import mock
import pytest
from diagram import empty_diagram, filled_diagram


@pytest.mark.parametrize("path", [os.path.abspath("./html"), os.path.abspath("/tmp")])
def test_empty_diagram(path):
    empty_diagram(path)


@pytest.mark.parametrize("aggregated", [True, False])
@mock.patch("diagram.diagram.get_weather_data")
@mock.patch("diagram.diagram.get_printable_forecast")
@mock.patch("diagram.diagram._create_diagram")
def test_filled_diagram(mock_create_diagram, mock_get_printable_forecast, mock_get_weather_data, aggregated):
    zip_code = "32216"
    data = {"data": "test_data"}
    mock_get_weather_data.return_value = data
    mock_get_printable_forecast.return_value = "Test Printable Forecast"

    filled_diagram(zip_code, aggregated=aggregated, data=None, path="/tmp")

    mock_get_weather_data.assert_called_once_with(zip_code)
    mock_get_printable_forecast.assert_called_once_with(data, aggregated=aggregated, sample=True)
    mock_create_diagram.assert_called_once_with(zip_code=zip_code, aggregated=aggregated,
                                                data_ex="Test Printable Forecast", path="/tmp")
