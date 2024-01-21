import requests
import time
from config import config

def get_api_key():
  config_data = config()

  if 'apikey' not in config_data:
    raise Exception('API key is missing in the configuration.')

  return config_data['apikey']

def get_time_zone():
  api_key = get_api_key()

  parameters = {
    'key': api_key,
    'format': 'json'
  }

  url = 'http://api.timezonedb.com/v2.1/list-time-zone'
  response = requests.get(url, params=parameters)

  if response.status_code == 200:
    return response.json()
  else:
    raise Exception("There was an error retrieving the data. ",  response.text)

def get_details(zones):
  api_key = get_api_key()

  parameters = {
    'key': api_key,
    'format': 'json',
    'by': 'zone',
    'zone': zones
  }

  url = 'http://api.timezonedb.com/v2.1/get-time-zone'
  response = requests.get(url, params=parameters)
  time.sleep(3)
  if response.status_code == 200:
    return response.json()
  else:
    raise Exception("There was an error retrieving the data. ",  response.text)
