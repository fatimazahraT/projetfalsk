import requests

class meteoApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_weather(self, city):
        params = {'q': city, 'appid': self.api_key}
        response = requests.get(self.base_url, params=params)
        return response.json()
