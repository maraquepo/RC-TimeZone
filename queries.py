import api
from datetime import datetime

def insert_into_timezones_list(json_data, cursor, connection):
  try:
    for response in json_data['zones']:
      current_time = datetime.now().strftime('%m-%d-%Y %H:%M:%S')

      cursor.execute(f'''
        INSERT INTO TZDB_TIMEZONES (COUNTRYCODE, COUNTRYNAME, ZONENAME, GMTOFFSET, IMPORT_DATE) VALUES ('{response['countryCode']}', '{response['countryName']}', '{response['zoneName']}', '{response['gmtOffset']}', '{current_time}');
                    ''')
  except Exception as e:
    print("There was an error inserting data into the timezone list table", e)
