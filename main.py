import sqlite3

def main():
  try:
    connection = sqlite3.connect('/timezone.db')
    cursor = connection.cursor()
  except Exception as e:
    print("There was an error creating the database")
    print(e)

  connection.commit()

if __name__ == "__main__":
  main()