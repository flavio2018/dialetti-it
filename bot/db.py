import sqlalchemy as sql
from config import DATABASE_URI


class DB:

    def __init__(self):
    	self.engine = sql.create_engine(DATABASE_URI)


    def get_regioni(self):

        SQL = "SELECT nome_regione FROM Regioni;"
        names = self.engine.execute(SQL)
        engine.close()

        return names

    def get_province(self, regione):
        pass

    def get_comuni(self, province):
        pass
