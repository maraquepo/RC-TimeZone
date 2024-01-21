import requests
from config import config

def get_time_zone():
  config_data = config()

  if 'apikey' not in config_data:
    raise Exception('API key is missing in the configuration.')

  api_key = config_data['apikey']
  url = f'http://api.timezonedb.com/v2.1/list-time-zone?key={api_key}&format=json'
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    raise Exception("There was an error retrieving the data. Status code: " + str(response.status_code))

