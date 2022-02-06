from typing import Callable, Any
from functools import wraps

from webcheck.utils import load_yaml
from webcheck.configuration import CollectorConfig, CONFIGURATION_FILE_PATH


def inject_configuration(function: Callable) -> Any:
    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        collector_config = __parse_config()
        return function(collector_config, *args, **kwargs)

    return wrapper


def __parse_config() -> CollectorConfig:
    return CollectorConfig(**load_yaml(CONFIGURATION_FILE_PATH))
