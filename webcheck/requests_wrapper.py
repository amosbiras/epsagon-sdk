import time

import requests

from dataclasses import dataclass, asdict
from uuid import uuid4
from datetime import datetime
from typing import Callable, Any, Tuple, Dict, NoReturn

from webcheck.configuration import CollectorConfig
from webcheck.utils.decorators import inject_configuration, exception_decorator


@dataclass
class RequestMetric:
    id: str
    timestamp: str
    duration: float
    target_url: str
    response_code: int


def collect_requests_metrics_wrapper(function: Callable[..., requests.Response], instance, args: Tuple,
                                     kwargs: Dict[str, Any]) -> requests.Response:
    timestamp = datetime.utcnow().replace(microsecond=0).isoformat()
    start_time = time.perf_counter()
    try:
        response = function(*args, **kwargs)
        __complete_metric_collection(start_time, args, kwargs, timestamp, response.status_code)
        return response
    except requests.RequestException as e:
        __complete_metric_collection(start_time, args, kwargs, timestamp, status_code=503)
        raise e


@exception_decorator
@inject_configuration
def __complete_metric_collection(collector_config: CollectorConfig, start_time: float, args: Tuple,
                                 kwargs: Dict[str, Any], timestamp: str, status_code: int) -> NoReturn:
    duration = time.perf_counter() - start_time
    target_url = __get_target_url(args, kwargs)
    request_metric = RequestMetric(id=str(uuid4()), timestamp=timestamp, duration=duration, target_url=target_url,
                                   response_code=status_code)
    server_response = requests.post(
        f'http://{collector_config.host}:{collector_config.port}/{collector_config.requests_metric_collection_endpoint}',
        json=asdict(request_metric))
    server_response.raise_for_status()


def __get_target_url(args: Tuple, kwargs: Dict[str, Any]) -> str:
    if kwargs:
        return kwargs['url']
    else:
        return args[0]
