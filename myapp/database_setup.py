import sqlite3

# Path to your database file
database_path = 'Mydata.db'

# Connect to SQLite database
conn = sqlite3.connect(database_path)

# Read SQL file
script_file = 'dump.sql'
with open(script_file, 'r') as file:
    script = file.read()

# Execute script
conn.executescript(script)
conn.close()
