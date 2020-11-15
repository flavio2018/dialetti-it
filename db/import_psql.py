import psycopg2
import csv

def load_data():
    # paths to data files
    regioni = '../Dati Geografici/regioni.csv'
    province = '../Dati Geografici/province.csv'
    comuni = '../Dati Geografici/comuni.csv'

    DB_USER = 'shift97'
    DB_PASS = ''
    DB_HOST = 'localhost'
    DB_NAME = 'dialetti_it'

    conn = psycopg2.connect("dbname=" + DB_USER + "user=" + DB_USER + "password= host=127.0.0.1")
