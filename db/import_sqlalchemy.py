import sqlalchemy as sql
import pandas as pd
from db.config import DATABASE_URI

# create the engine and the connection
engine = sql.create_engine(DATABASE_URI)

# paths to data files
regioni = './Dati Geografici/regioni.csv'
province = './Dati Geografici/province.csv'
comuni = './Dati Geografici/comuni.csv'

# read .csv files
df = pd.read_csv(regioni, names=['codice_nuts2', 'nome_regione'], skiprows=1)

# dump to sql
df.to_sql('regioni', engine, if_exists='append', index=False)

# same for the other tables
cols = ['codice_nuts3', 'nome_provincia', 'nuts2_regione']
df = pd.read_csv(province, names=cols, skiprows=1)
df.to_sql('province', engine, if_exists='append', index=False, method='multi')

cols = ['id_comune', 'nome_comune', 'nuts3_provincia', 'longitudine_comune', 'latitudine_comune']
df = pd.read_csv(comuni, names=cols, skiprows=1)
df.to_sql('comuni', engine, if_exists='append', index=False, method='multi')

# check table
pd.read_sql('SELECT * FROM comuni;', engine).head()
