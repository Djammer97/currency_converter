import secrets
from abc import ABC, abstractmethod


class AbstractRepo(ABC):
    @abstractmethod
    async def add_data(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def get_data_by_key(self, key, value):
        raise NotImplementedError


class RepoListDicts(AbstractRepo):
    data_list_dicts: list = None

    async def add_data(self, data: dict):
        self.data_list_dicts.append(data)

    async def get_data_by_key(self, key, value) -> dict:
        for one_data in self.data_list_dicts:
            if key in one_data and secrets.compare_digest(one_data[key], value):
                return one_data
