from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists,create_database
from .ConnectionStringAdapterModule import ConnectionStringAdapter
from lib.dtos.todo import Todo, Base


class ConnectionFactory(object):
    # initialize connection helper with connection string
    def __init__(self, connection_adapter: ConnectionStringAdapter = None):
        self.adapter = connection_adapter
        self.engine = create_engine(self.adapter.getConnectionString(), echo=True)

        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        print('should create database here')
        Base.metadata.create_all(bind=self.engine, checkfirst=True)

    # get SqlAchemy Database Engine using this function
    def getEngine(self):
        try:
            # self.engine = create_engine(self.adapter.getConnectionString())
            return self.engine
        except Exception as engex:
            print(engex)

    # get connection object after connecting with database through engine
    def getConnection(self):
        try:
            return self.engine.connect()
        except Exception as ex:
            print(ex)