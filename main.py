import sqlite3
import create_tables

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
    connection.commit()
  except Exception as e:
    print("There was an error creating the tables")
    print(e)

if __name__ == "__main__":
  main()