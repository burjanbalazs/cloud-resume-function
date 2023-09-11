import logging
import os


from azure.cosmosdb.table import TableService, Entity
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')

    cosmosdb_connection_string = os.environ['CosmosDB_connection_string']
    table_name = "Visitors"
    query_filter = "PartitionKey eq '1'"
    table_service = TableService(endpoint_suffix = "table.cosmos.azure.com", connection_string= cosmosdb_connection_string)
    entities = table_service.query_entities(table_name=table_name, filter=query_filter)

    for entity in entities:
        count = entity['VisitorCount'].value


    return func.HttpResponse(
            f"{count}",
            status_code=200
    )
