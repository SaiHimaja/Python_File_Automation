import pytest
from main import getWeather

def test_weather(mocker):
    mock_get=mocker.patch("main.requests.get")
    mock_get.return_value.status_code=200
    mock_get.return_value.json.return_value={"temperature":25,"condition":"Sunny"}

    result=getWeather("Dubai")

    assert result== {"temperature":25,"condition":"Sunny"}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")

    
    