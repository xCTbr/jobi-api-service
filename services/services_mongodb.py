import boto3
import json
from pymongo import MongoClient


def connectCursosCollection():
    # Gets MongoDB Credentials
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name='us-east-1')

    secret_response = client.get_secret_value(
        SecretId='mongodb/service-user/credentials')
    mongo_credentials = json.loads(secret_response['SecretString'])

    mongo_user = mongo_credentials['user']
    mongo_password = mongo_credentials['password']

    # Instatiate MongoDB Client
    mongo_conn_string = f'mongodb+srv://{mongo_user}:{mongo_password}@jobi-cluster.bc1kiqp.mongodb.net/?retryWrites=true&w=majority'

    cluster = MongoClient(mongo_conn_string)
    db = cluster["jobi-principal"]
    collection = db["cursos"]

    return collection
