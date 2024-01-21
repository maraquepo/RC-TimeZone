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

def create_details_table(cursor):
  try:
    cursor.execute('''
      CREATE TABLE TZDB_ZONE_DETAILS (
        COUNTRYCODE VARCHAR2(2) NOT NULL,
        COUNTRYNAME VARCHAR2(100) NOT NULL,
        ZONENAME VARCHAR2(100) NOT NULL,
        GMTOFFSET NUMBER NOT NULL,
        DST NUMBER NOT NULL,
        ZONESTART NUMBER NOT NULL,
        ZONEEND NUMBER NOT NULL,
        IMPORT_DATE DATE,
        PRIMARY KEY (ZONENAME, ZONESTART, ZONEEND)
      );
                  ''')

  except sqlite3.OperationalError as e:
    pass
  except Exception as e:
    print(e)

def create_error_table(cursor):
  try:
    cursor.execute('''
      CREATE TABLE TZDB_ERROR_LOG (
        ERROR_DATE DATE,
        ERROR_MESSAGE VARCHAR2(1000)
      );
                  ''')

  except sqlite3.OperationalError as e:
    pass
  except Exception as e:
    print(e)
