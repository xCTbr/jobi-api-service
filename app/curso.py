import json
import services.services_mongodb as mg_services


def getCursos(event, context):

    collection = mg_services.connectCursosCollection()

    results = collection.find({})

    list_cursos = []
    for x in results:
        list_cursos.append(x)

    body = {
        "resultado": list_cursos
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


def getCurso(event, context):

    collection = mg_services.connectCursosCollection()

    curso_id = int(event['pathParameters']['cursoId'])

    result = collection.find_one({"_id": curso_id})

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
