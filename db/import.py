import mysql.connector
import csv

# paths to data files
regioni = '../Dati Geografici/regioni.csv'
province = '../Dati Geografici/province.csv'
comuni = '../Dati Geografici/comuni.csv'

# db credentials
DB_USER = 'root'
DB_PASS = 'password'
DB_HOST = 'localhost'
DB_NAME = 'dialetti_it'

conn = mysql.connector.connect(
    user = DB_USER,
    password = DB_PASS,
    host = DB_HOST,
    database = DB_NAME)

cursor = conn.cursor()

with open(regioni, 'r') as csv_data:
    reader = csv.reader(csv_data, delimiter=',')
    csv_data_list = list(reader)
    for i, row in enumerate(csv_data_list):
        if i != 0:
            cursor.execute("""
                INSERT INTO Regioni
                VALUES (%s, %s)""",
                (row[0], row[1]))
conn.commit()
print("Regioni inserite ✓")

with open(province, 'r') as csv_data:
    reader = csv.reader(csv_data, delimiter=',')
    csv_data_list = list(reader)
    for i, row in enumerate(csv_data_list):
        if i != 0:
            cursor.execute("""
                INSERT INTO Province
                VALUES (%s, %s, %s)""",
                (row[0], row[1], row[2]))
conn.commit()
print("Province inserite ✓")
            
with open(comuni, 'r') as csv_data:
    reader = csv.reader(csv_data, delimiter=',')
    csv_data_list = list(reader)
    for i, row in enumerate(csv_data_list):
        if i != 0:
            cursor.execute("""
                INSERT INTO Comuni
                VALUES (%s, %s, %s, %s, %s)""", # %s does not mean string
                (row[0], row[1], row[2], row[3], row[4]))

conn.commit()
print("Comuni inseriti ✓")

cursor.close()
conn.close()
print("Fatto!")
