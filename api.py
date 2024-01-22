import requests
import time
from config import config

def get_api_key():
  # Get the API key from the configuration
  config_data = config()
  # Check if 'apikey' is present in the configuration
  if 'apikey' not in config_data:
    raise Exception('API key is missing in the configuration.')

  return config_data['apikey']

def get_time_zone():
  # Get the API key
  api_key = get_api_key()
  # Set parameters for the list-time-zone API request
  parameters = {
    'key': api_key,
    'format': 'json'
  }
  # Define the URL for the list-time-zone API endpoint
  url = 'http://api.timezonedb.com/v2.1/list-time-zone'
  # Make the API request
  response = requests.get(url, params=parameters)
  # Check the response status code
  if response.status_code == 200:
    # Return the JSON data if the request is successful
    return response.json()
  else:
    raise Exception("There was an error retrieving the data. ",  response.text)

def get_details(zones):
  # Get the API key
  api_key = get_api_key()
  # Set parameters for the get-time-zone API request
  parameters = {
    'key': api_key,
    'format': 'json',
    'by': 'zone',
    'zone': zones
  }
  # Define the URL for the get-time-zone API endpoint
  url = 'http://api.timezonedb.com/v2.1/get-time-zone'
  # Make the API request with a delay of 2 seconds
  response = requests.get(url, params=parameters)
  time.sleep(2)
  # Check the response status code
  if response.status_code == 200:
    # Return the JSON data if the request is successful
    return response.json()
  else:
    raise Exception("There was an error retrieving the data. ",  response.text)
