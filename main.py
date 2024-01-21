import sqlite3
import create_tables
import api
import queries

def main():
  try:
    connection = sqlite3.connect('./timezone.db')
    cursor = connection.cursor()
  except Exception as e:
    print("There was an error creating the database")
    print(e)

  try:
    create_tables.create_timezone_table(cursor)
    create_tables.create_details_table(cursor)
    create_tables.create_error_table(cursor)
    connection.commit()
  except Exception as e:
    print("There was an error creating the tables")
    print(e)

  try:
    time_zone_data = api.get_time_zone()
    # Insert data into database
    queries.insert_into_timezones_list(time_zone_data, cursor, connection)
  except Exception as e:
    print("There was an error retreiving data or inserting into table", e)

  try:
    zone_details_list = cursor.execute(''' SELECT ZONENAME FROM TZDB_ZONE_DETAILS; ''').fetchall()

    zone_list = [zone[0] for zone in zone_details_list]

  except Exception as e:
    print("There was an error retreiving data or inserting into table", e)

  try:
    queries.insert_into_zone_details(time_zone_data, zone_list, cursor, connection)
  except Exception as e:
    print("There was an error retreiving data or inserting into table", e)

  connection.commit()

if __name__ == "__main__":
  main()