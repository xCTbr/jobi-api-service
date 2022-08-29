import json


def hello(event, context):
    body = {
        "message": "Bem Vindo ao Jobi!",
        # "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
