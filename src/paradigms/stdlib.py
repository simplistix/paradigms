from collections.abc import Callable

from .core import Paradigm


class Simple[**P, T](Paradigm):

    def __call__(self, callable_: Callable[P, T], /, *args: P.args, **kwargs: P.kwargs) -> T:
        return callable_(*args, **kwargs)
