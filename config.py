from configparser import ConfigParser

def config(filename="api_config.ini", section="api"):
  parser = ConfigParser()
  parser.read(filename)
  config_data = {}

  if parser.has_section(section):
    params = parser.items(section)
    for param in params:
      config_data[param[0]] = param[1]
  else:
    raise Exception('Section {0} is not found in the {1} file.'.format(section,filename))

  return config_data
