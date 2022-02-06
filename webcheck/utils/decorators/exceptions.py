import logging

import requests

from typing import Callable, Any
from functools import wraps

logger = logging.getLogger(__name__)


def exception_decorator(function: Callable) -> Any:
    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            result = function(*args, **kwargs)
            return result
        except requests.RequestException as e:
            logger.error(f'{type(e).__name__} - {e}', exc_info=True,
                         extra={'exception_type': type(e).__name__, 'exception': e})
    return wrapper
