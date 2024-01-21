import sqlite3

def create_timezone_table(cursor):
  try:
    cursor.execute('''
      CREATE TABLE TZDB_TIMEZONES (
        COUNTRYCODE VARCHAR2(2) NOT NULL,
        COUNTRYNAME VARCHAR2(100) NOT NULL,
        ZONENAME VARCHAR2(100) PRIMARY KEY,
        GMTOFFSET NUMBER,
        IMPORT_DATE DATE
      );
                  ''')

  except sqlite3.OperationalError as e:
    pass
  except Exception as e:
    print(e)
