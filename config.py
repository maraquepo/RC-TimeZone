from configparser import ConfigParser

def config(filename="api_config.ini", section="api"):
  # Create a ConfigParser object to read the configuration file
  parser = ConfigParser()
  # Read the configuration file
  parser.read(filename)
  # Initialize an empty dictionary to store configuration data
  config_data = {}
  # Check if the specified section exists in the configuration file
  if parser.has_section(section):
    # Iterate over the parameters in the specified section
    params = parser.items(section)
    for param in params:
      # Store each parameter in the config_data dictionary
      config_data[param[0]] = param[1]
  else:
    raise Exception('Section {0} is not found in the {1} file.'.format(section,filename))

  return config_data
