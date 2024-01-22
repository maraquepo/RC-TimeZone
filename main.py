import sqlite3
import create_tables
import api
import queries

def main():
  # Display loading message as the script is running
  print("Loading data...")
  print("Press Cltr+C to stop script.")

  try:
    # Establish a connection to the SQLite database
    connection = sqlite3.connect('./timezone.db')
    cursor = connection.cursor()
  except Exception as e:
    print("There was an error creating the database")
    print(e)

  try:
    # Delete TZDB_TIMEZONES table if it exists every time script runs
    create_tables.delete_timezone_table(cursor)
    # Create tables in the database
    create_tables.create_timezone_table(cursor)
    create_tables.create_details_table(cursor)
    create_tables.create_error_table(cursor)
    connection.commit()
  except Exception as e:
    queries.insert_into_error_table("There was an error creating the tables:" + str(e), cursor, connection)

  try:
    # Fetch time zone data from TimeZone API
    time_zone_data = api.get_time_zone()
    # Insert time zone data into the database
    queries.insert_into_timezones_list(time_zone_data, cursor, connection)
  except Exception as e:
    queries.insert_into_error_table("There was an error retreiving data or inserting into time zone table" + str(e), cursor, connection)

  try:
    # Fetch zone details list from database to ensure we don't add rows if the data in the table already exists
    zone_details_list = cursor.execute(''' SELECT ZONENAME FROM TZDB_ZONE_DETAILS; ''').fetchall()
    # Extract the ZONENAME (or first element) from each tuple in zone_details_list
    zone_list = [zone[0] for zone in zone_details_list]

  except Exception as e:
    queries.insert_into_error_table("There was an error fetching data from zone details table" + str(e), cursor, connection)

  try:
    # Insert time zone details into database
    queries.insert_into_zone_details(time_zone_data, zone_list, cursor, connection)
  except Exception as e:
    queries.insert_into_error_table("There was an error retreiving data or inserting into zone details table" + str(e), cursor, connection)

  # Commit changes to the database
  connection.commit()

if __name__ == "__main__":
  main()
