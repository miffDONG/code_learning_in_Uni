import os
import io
import boto3
import json
import csv
import numpy as np
import pandas as pd

ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    data = json.loads(json.dumps(event))
    payload = data['data']
    print(payload)
    
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body=payload)
                                       
    result = json.dumps([response['Body'].read().decode()])
    # # print(response)
    # # result = json.loads(response['Body'].read().decode())
    # response = json.dumps(response['Body'])
    # print(f"response {response}")
    # print(f"response.read {response.read()}")
    
    # print(f"response.read.decode {response.read().decode}")
    print(result)
    
    
    return result
    