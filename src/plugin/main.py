from typing import Generator
from spaceone.inventory.plugin.collector.lib.server import CollectorPluginServer

app = CollectorPluginServer()

@app.route("Collector.init")
def collector_init(params: dict) -> dict:
    return

@app.route("Collector.collect")
def collector_collect(params: dict) -> Generator[dict, None, None]:
    options = params["options"]
    secret_data = params["secret_data"]
    schema = params.get("schema")
    
    