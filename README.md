# RC-TimeZone

This project interacts with the TimeZoneDB API to fetch and store time zone information in an SQLite database.

## Getting Started

### Prerequisites

- Python 3
- SQLite

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/maraquepo/RC-TimeZone.git
   cd RC-TimeZone


## Project Structure

- **main.py:** Script to initialize the project and interact with the database.
- **create_tables.py:** Module to create database tables.
- **queries.py:** Module with functions to insert data into the database.
- **config.py:** Module to read configuration data from an INI file.
- **api.py:** Module to interact with the TimeZoneDB API.
- **api_config.ini:** Configuration file for API keys.

## Usage

1. Run the `main.py` script:

   ```bash
   python main.py

2. The script will load data from the TimeZoneDB API and store it in the SQLite database.

## Configuration
Edit the api_config.ini.sample file to provide the required API key and remove '.sample' from the file name.

## Planning
![image](https://github.com/maraquepo/RC-TimeZone/assets/86852189/651e2f4a-c688-4c42-8a6e-0092ff4384a2)

## Interacting with the SQLite3 Database

Before interacting with the SQLite3 database file (`timezone.db`), make sure to run the `main.py` script to load data from the TimeZoneDB API and store it in the SQLite database.

Once the script has been executed, you can use the `sqlite3` command-line tool to interact with the database. For example:

### Open the SQLite3 shell:

```bash
sqlite3 timezone.db
```

### Show tables of the database:

```bash
.tables
```
### Interact with database:

Examples:

```bash
SELECT * FROM TZDB_TIMEZONES LIMIT 2;
SELECT * FROM TZDB_ZONE_DETAILS LIMIT 2;
```

![image](https://github.com/maraquepo/RC-TimeZone/assets/86852189/5ba8680d-85f5-46bd-a116-b83bcfd32971)


### Exit the SQLite3 shell
```bash
.exit


