import api
from datetime import datetime

def insert_into_error_table(message, cursor, connection):
  # Formats current date to match (01/21/2024 06:00:00 PM)
  current_time = datetime.now().strftime('%m/%d/%Y %I:%M:%S %p')
  # Insert an error message along with the current date into the error log table
  cursor.execute(f'''
                  INSERT INTO TZDB_ERROR_LOG (ERROR_DATE, ERROR_MESSAGE) VALUES ('{current_time}', '{message}');
                ''')
  connection.commit()

def insert_into_timezones_list(json_data, cursor, connection):
  try:
    for response in json_data['zones']:
      # Formats current date to match (01/21/2024 06:00:00 PM)
      current_time = datetime.now().strftime('%m/%d/%Y %I:%M:%S %p')
      # Insert timezone data into the timezones table
      cursor.execute(f'''
        INSERT INTO TZDB_TIMEZONES (COUNTRYCODE, COUNTRYNAME, ZONENAME, GMTOFFSET, IMPORT_DATE) VALUES ('{response['countryCode']}', '{response['countryName']}', '{response['zoneName']}', '{response['gmtOffset']}', '{current_time}');
                    ''')
  except Exception as e:
    insert_into_error_table("Timezone List Insert Error: " + str(e), cursor, connection)

def insert_into_zone_details(json_data, known_zones, cursor, connection):
  try:
    for response in json_data['zones']:
      # If zonename exists in the database, then skip it
      if response['zoneName'] in known_zones:
        continue
      try:
        # Formats current date to match (01/21/2024 06:00:00 PM)
        current_time = datetime.now().strftime('%m/%d/%Y %I:%M:%S %p')
        # Retrieve detailed zone information from the API
        zone_details_response = api.get_details(response['zoneName'])
        # Insert zone details into the zone details table
        cursor.execute(f'''
          INSERT INTO TZDB_ZONE_DETAILS (COUNTRYCODE, COUNTRYNAME, ZONENAME, GMTOFFSET, DST, ZONESTART, ZONEEND, IMPORT_DATE) VALUES ( '{zone_details_response['countryCode']}', '{zone_details_response['countryName']}', '{zone_details_response['zoneName']}', '{zone_details_response['gmtOffset']}', '{zone_details_response['dst']}', '{zone_details_response['zoneStart']}', '{zone_details_response['zoneEnd']}', '{current_time}' );
                      ''')
        connection.commit()
      except Exception as e:
        insert_into_error_table("Zone Details Insert Error: " + str(e), cursor, connection)

  except Exception as e:
    insert_into_error_table("Zone Details Insert Error: " + str(e), cursor, connection)
