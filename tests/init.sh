#!/bin/bash


aws dynamodb delete-table \
     --endpoint-url=http://localhost:4569 \
     --profile localstack \
     --table-name TestTable

aws dynamodb create-table \
     --endpoint-url=http://localhost:4569 \
     --profile localstack \
     --table-name TestTable \
     --attribute-definitions \
         AttributeName=id,AttributeType=S \
     --key-schema AttributeName=id,KeyType=HASH \
     --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1

data='{
        "id": {"S": "1a2b"},
        "name": {"S": "take"},
        "created_at": {"N": "1520400553"},
        "updated_at": {"N": "1520400554"}
      }'

aws dynamodb put-item \
     --endpoint-url=http://localhost:4569 \
     --profile localstack \
     --table-name TestTable \
      --item "${data}"

aws dynamodb scan \
     --endpoint-url=http://localhost:4569 \
     --profile=localstack \
     --table-name TestTable
