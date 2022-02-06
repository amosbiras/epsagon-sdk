import wrapt
import requests

from webcheck.requests_wrapper import collect_requests_metrics_wrapper

wrapt.wrap_function_wrapper(requests, 'get', collect_requests_metrics_wrapper)
