import sys
from collections.abc import Callable
from typing import Any

import typer

ExceptionType = type[Exception]
ErrorHandlingCallback = Callable[[Exception], None]


class InstantPythonTyper(typer.Typer):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.error_handlers: dict[ExceptionType, ErrorHandlingCallback] = {}

    def error_handler(self, exc: ExceptionType) -> Callable[[Callable[[Exception], None]], Callable[[Exception], None]]:
        """Registers a callback function to be called when 'exc' (the given exception) is raised."""

        def decorator(func: ErrorHandlingCallback) -> Callable[[Exception], None]:
            self.error_handlers[exc] = func
            return func

        return decorator

    def __call__(self, *args, **kwargs) -> Any:
        """Overrides Typer.__call__ so that when we run the CLI,
        we can catch any exception that's raised and see if there's
        a matching error handler for it.
        """
        try:
            super().__call__(*args, **kwargs)
        except Exception as error:
            handler = self._find_handler(error)
            if handler is None:
                raise
            handler(error)
            sys.exit(1)

    def _find_handler(self, error: Exception) -> ErrorHandlingCallback | None:
        """Walks the error's MRO so the most specific registered handler
        always wins, regardless of the order handlers were registered in.
        """
        for exc_type in type(error).__mro__:
            if exc_type in self.error_handlers:
                return self.error_handlers[exc_type]
        return None
