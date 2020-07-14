from lib.repositories.TodoRepository import *
from lib.helpers.ConnectionFactoryModule import *
from lib.helpers.ConnectionStringAdapterModule import *
from sqlalchemy.orm import sessionmaker


class UnitOfWork(object):
    def __init__(self, adapter: ConnectionStringAdapter = None):
        # get adapter
        self.connectionAdapter = adapter
        # get connection
        factory = ConnectionFactory(self.connectionAdapter)
        # bind the engine with session
        Session = sessionmaker(bind=factory.getEngine())
        # pass the session object to the repositories
        self.todoRepo = TodoRepository(Session())
