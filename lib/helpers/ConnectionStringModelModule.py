class ConnectionStringModel(object):
    def __init__(self, username=None, password=None, host=None, database=None, db_url=None):
        self.username = username
        self.password = password
        self.host = host
        self.database = database
        self.db_url = db_url