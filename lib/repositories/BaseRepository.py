import uuid


class BaseRepository(object):
    # initialize base repository
    # session is the Session Object from sessionmaker
    # queryType is the type of object/ domain model/ table in question
    # hasGuidPrimarykey determins if the quried table has a GUID as Primary key or not
    def __init__(self, session, query_type, has_uuid_primary_key: bool = False):
        self._session = session
        self.has_guid_as_primary = has_uuid_primary_key
        self.query_type = query_type

    # this method gets all the shit from database table
    def get_all(self):
        try:
            res = self._session.query(self.query_type).all()
            return res
        except Exception as ex:
            print(ex)

    # Insert object in database
    def create(self, obj):
        try:
            # if the primary key is guid then it generates and inserts it
            if self.has_guid_as_primary: obj.id = self.generate_unique_id()

            self._session.add(obj)
            self._session.commit()
        except Exception as ex:
            print(ex)

    # Update
    def update(self, id, obj):
        try:
            self._session.query(self.query_type).filter(self.query_type.id == id).update(obj, synchronize_session=False)
                # .update({Customers.name: "Mr." + Customers.name}, synchronize_session=False)
            self._session.commit()
        except Exception as ex:
            print(ex)

    # delete a complete object
    def delete(self, obj):
        try:
            m = self.get_by_id(obj.id)
            self._session.delete(m)
            res = self._session.commit()
            return res
        except Exception as ex:
            print(ex)

    # Get single object from db based on id
    def get_by_id(self, id):
        try:
            res = self._session.query(self.query_type).filter(self.query_type.id == id)
            return res[0]
        except Exception as ex:
            print(ex)

    # generates a Guid for inserting shit in sql server with a GUID as a primary key
    @staticmethod
    def generate_unique_id():
        return str(uuid.uuid4())
