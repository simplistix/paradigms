from collections.abc import Callable
from concurrent.futures import Future

from typing_extensions import Protocol

from .core import Paradigm


class Simple[**P, T](Paradigm[P, T]):
    pass

#    def __call__(self, callable_: Callable[P, T], /, *args: P.args, **kwargs: P.kwargs) -> T:
#       return callable_(*args, **kwargs)
#
#
# class Async[**P, T: Coroutine](Paradigm):
#
#     async def __call__(self, callable_: Callable[P, T], /, *args: P.args, **kwargs: P.kwargs) -> Awaitable[T]:
#         return await callable_(*args, **kwargs)
#
#
# class ConcurrentFutures[**P, T](Paradigm, Protocol):
#
#     def __call__(self, callable_: Callable[P, T], /, *args: P.args, **kwargs: P.kwargs) -> Future[T]:
#         pass
