import api
from datetime import datetime

def insert_into_error_table(message, cursor, connection):
  current_time = datetime.now().strftime('%m-%d-%Y %H:%M:%S')
  cursor.execute(f'''
                  INSERT INTO TZDB_ERROR_LOG (ERROR_DATE, ERROR_MESSAGE) VALUES ('{current_time}', '{message}');
                ''')
  connection.commit()

def insert_into_timezones_list(json_data, cursor, connection):
  try:
    for response in json_data['zones']:
      current_time = datetime.now().strftime('%m-%d-%Y %H:%M:%S')

      cursor.execute(f'''
        INSERT INTO TZDB_TIMEZONES (COUNTRYCODE, COUNTRYNAME, ZONENAME, GMTOFFSET, IMPORT_DATE) VALUES ('{response['countryCode']}', '{response['countryName']}', '{response['zoneName']}', '{response['gmtOffset']}', '{current_time}');
                    ''')
  except Exception as e:
    insert_into_error_table("Timezone List Insert Error: " + str(e), cursor, connection)

def insert_into_zone_details(json_data, known_zones, cursor, connection):
  try:
    for response in json_data['zones']:
      if response['zoneName'] in known_zones:
        continue
      try:
        current_time = datetime.now().strftime('%m-%d-%Y %H:%M:%S')
        zone_details_response = api.get_details(response['zoneName'])
        cursor.execute(f'''
          INSERT INTO TZDB_ZONE_DETAILS (COUNTRYCODE, COUNTRYNAME, ZONENAME, GMTOFFSET, DST, ZONESTART, ZONEEND, IMPORT_DATE) VALUES ( '{zone_details_response['countryCode']}', '{zone_details_response['countryName']}', '{zone_details_response['zoneName']}', '{zone_details_response['gmtOffset']}', '{zone_details_response['dst']}', '{zone_details_response['zoneStart']}', '{zone_details_response['zoneEnd']}', '{current_time});
                      ''')
        connection.commit()
      except Exception as e:
        insert_into_error_table("Zone Details Insert Error: " + str(e), cursor, connection)

  except Exception as e:
    insert_into_error_table("Zone Details Insert Error: " + str(e), cursor, connection)

