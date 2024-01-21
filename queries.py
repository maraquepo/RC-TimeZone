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


