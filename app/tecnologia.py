import json
import services.services_mongodb as mg_services


def getTecnologias(event, context):

    collection = mg_services.connectTecnologiasCollection()

    results = collection.find({})

    list_tecnologias = []
    for x in results:
        list_tecnologias.append(x)

    body = {
        "resultado": list_tecnologias
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": 'true',
        }
    }

    return response
