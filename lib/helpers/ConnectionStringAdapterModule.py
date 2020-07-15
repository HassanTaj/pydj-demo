import urllib
from .ConnectionTypeModule import ConnectionType
from .ConnectionStringModelModule import ConnectionStringModel


class ConnectionStringAdapter(object):
    def __init__(self, connection_string_obj: ConnectionStringModel = None, connection_type: ConnectionType = None):
        self.conString = ''
        self.connectionType = connection_type
        self.conS = connection_string_obj
        # for Sqlite connection based on a database url
        if self.connectionType == ConnectionType.sql_lite:
            # path to sqlite.db file
            self.conString = f'sqlite:///{self.conS.db_url}'
        # for mssql connection based on credentials
        elif self.connectionType == ConnectionType.ms_sql:
            # TODO: solve this connection string or dirver issue wtf is this man.
            # mssql connection string
            con = f"""
            DRIVER={{SQL Server}};
            SERVER={self.conS.host}:1443;
            DATABASE={self.conS.database};
            UID={self.conS.username};
            PWD={self.conS.password};
            """
            # Trusted_Connection = yes;
            params = urllib.parse.quote_plus(con)
            # self.conString = params
            self.conString = "mssql+pyodbc:///?odbc_connect=%s" % params
            # self.conString = "mssql+pyodbc://%s" % params
            # self.conString = f"""mssql+pyodbc:///?odbc_connect={self.conS.username}:{self.conS.password}@{self.conS.host}:1433/{self.conS.database}"""
            # self.conString = f"""mssql+pyodbc:///{self.conS.username}:{self.conS.password}@{self.conS.host}:1433/{self.conS.database}?driver=SQL+Server"""
        # for postgress sql based on credidentials
        elif self.connectionType == ConnectionType.postgres_sql:
            # username:password@host/databasename
            con = f"""{self.conS.username}:{self.conS.password}@{self.conS.host}/{self.conS.database}"""
            params = urllib.parse.quote_plus(con)
            print(con)
            self.conString = f"""postgresql://{con}"""

    # connection string builder
    def getConnectionString(self):
        return self.conString
