from pydantic import BaseModel

CONFIGURATION_FILE_PATH = './etc/settings/collector.yaml'


class CollectorConfig(BaseModel):
    host: str
    port: int
    requests_metric_collection_endpoint: str
