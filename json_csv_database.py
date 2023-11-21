import requests
from datetime import datetime
import sqlite3
import csv
import pandas as pd

current_date = datetime.now().strftime("%d-%b-%Y")

url = f"https://www.smartgriddashboard.com/DashboardService.svc/data?area=windactual&region=ALL&datefrom={current_date}+00%3A00&dateto={current_date}+23%3A59"
response = requests.get(url)
data_json = response.json()

csv_name = f"{current_date}windActualDemand.csv"
df = pd.DataFrame(data_json['Rows'], columns=['EffectiveTime', 'FieldName', 'Region', 'Value'])

# Save the DataFrame to CSV
df.to_csv(csv_name, index=False)

# Create SQLite connection and cursor
conn = sqlite3.connect('windActualDemand.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS windDemand (
        EffectiveTime DATETIME,
        FieldName TEXT,
        Region TEXT,
        Value FLOAT
    );
''')

# Read the CSV file into the SQLite table
with open(csv_name, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO windDemand (EffectiveTime, FieldName, Region, Value) 
            VALUES (?, ?, ?, ?)
        ''', row)

# Commit the changes and close the connection
conn.commit()
conn.close()
