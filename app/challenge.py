import json
import services.services_mongodb as mg_services


def getChallenges(event, context):

    collection = mg_services.connectChallengesCollection()

    tecnologia_id = int(event['pathParameters']['tecnologiaId'])

    result = collection.find({"tecnologiaId": tecnologia_id})

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


def getChallenge(event, context):

    collection = mg_services.connectChallengesCollection()

    tecnologia_id = int(event['pathParameters']['tecnologiaId'])
    challenge_id = int(event['pathParameters']['challengeId'])

    result = collection.find_one({"tecnologiaId": tecnologia_id,
                                  "_id": challenge_id})

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
