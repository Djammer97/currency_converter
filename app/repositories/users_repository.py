from app.db.database import users
from app.repositories.base_repository import AbstractRepo, RepoListDicts


class UserRepo(RepoListDicts):
    data_list_dicts = users
