"""This is python3.6 program."""

import boto3
import datetime
import uuid
from builtins import Exception
import os
import time
from src.functions.utils import *

DYNAMODB_ENDPOINT = os.getenv('DYNAMODB_ENDPOINT')
TEST_TABLE_NAME = os.getenv('TEST_TABLE_NAME')

print(DYNAMODB_ENDPOINT)
print(TEST_TABLE_NAME)

DYNAMO = boto3.resource(
    'dynamodb',
    endpoint_url=DYNAMODB_ENDPOINT
)

DYNAMODB_TABLE = DYNAMO.Table(TEST_TABLE_NAME)


def get(event, context):
    try:
        user_id = event['pathParameters']['userId']

        dynamo_response = DYNAMODB_TABLE.get_item(
            Key={
                'id': user_id
            }
        )

        response = {
            "statusCode": 200 ,
            "body": json.dumps(response)
        }

        return response

    except Exception as error:
        raise error


def put(event, context):
    try:
        user_id = str(uuid.uuid4())

        name = event.get('name')
        updated_at = epoc_by_second_precision(datetime.now())

        response = DYNAMODB_TABLE.put_item(
            Item={
                'id': user_id,
                'name': name,
                'updated_at': updated_at,
                'created_at': updated_at,
            }
        )
        time.sleep(1)
        response = {
            "statusCode": 200 ,
            "body": json.dumps(response)
        }
        return response
    except Exception as error:
        raise error
