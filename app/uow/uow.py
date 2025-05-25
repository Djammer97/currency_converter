import asyncio
from abc import ABC, abstractmethod

import aiohttp


class IUnitOfWork(ABC):
    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self):
        ...


class UnitOfWork(IUnitOfWork):
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *args):
        await self.session.close()
        self.session = None
