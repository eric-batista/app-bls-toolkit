import asyncio
from fastapi import FastAPI
from typing import Callable, Awaitable, Coroutine
from starlette.datastructures import State


def on_event(app: FastAPI, *handlers: Callable[[State], Awaitable[None]]) -> Callable[[], Coroutine[None, None, None]]:
    async def _setup_event():
        if handlers:
            await asyncio.gather(*(handler(app.state) for handler in handlers))

    return _setup_event
