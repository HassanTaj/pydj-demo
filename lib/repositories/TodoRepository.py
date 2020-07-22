from lib.dtos.todo import Todo
from lib.repositories.BaseRepository import BaseRepository


class TodoRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        # initialize base repository
        super().__init__(self.session, Todo, True)