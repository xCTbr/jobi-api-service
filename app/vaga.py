import json
import services.services_mongodb as mg_services


def getVagas(event, context):

    collection = mg_services.connectVagasCollection()

    results = collection.find({})

    list_vagas = []
    for x in results:
        list_vagas.append(x)

    body = {
        "resultado": list_vagas
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


def getVaga(event, context):

    collection = mg_services.connectVagasCollection()

    vaga_id = int(event['pathParameters']['vagaId'])

    result = collection.find_one({"_id": vaga_id})

    body = {
        "resultado": result
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
