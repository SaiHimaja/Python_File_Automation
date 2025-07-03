from main import getWeather

def test_getWeather():
    assert getWeather(21)== "hot"
    assert getWeather(12)=="cold"
