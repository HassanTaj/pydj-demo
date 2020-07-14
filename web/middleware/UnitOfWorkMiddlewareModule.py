from django.utils.deprecation import MiddlewareMixin

from lib.helpers.ConnectionStringAdapterModule import ConnectionStringAdapter
from lib.helpers.ConnectionStringModelModule import ConnectionStringModel
from lib.helpers.ConnectionTypeModule import ConnectionType
from lib.uow.UnitOfWorkModule import UnitOfWork
from web.config import settings


class UnitOfWorkMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        self.uow: UnitOfWork = UnitOfWork(ConnectionStringAdapter(
            ConnectionStringModel(
                username=settings.DATABASE['user'],
                password=settings.DATABASE['password'],
                host=settings.DATABASE['host'],
                database=settings.DATABASE['database'],
                db_url=settings.SQLITE_DATABASE["url"]
            ), ConnectionType.sql_lite))
        # One-time configuration and initialization.

    def process_request(self, request):
        request.uow = self.uow
        return None

    # def process_response(self, request, response):
    #     try:
    #         session = request.db_session
    #     except AttributeError:
    #         return response
    #     try:
    #         session.commit()
    #         return response
    #     except:
    #         # session.rollback()
    #         raise

# def process_exception(self, request, exception):
#     try:
#         session = request.db_session
#     except AttributeError:
#         return
# # session.rollback()
