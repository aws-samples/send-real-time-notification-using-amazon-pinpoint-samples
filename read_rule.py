"""
This module reads the transaction_alert_rule table to  high value transaction threshold

"""
import boto3
from botocore.exceptions import ClientError
def get_premium_rule(transaction_type, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('transaction_alert_rule')

    try:
        response = table.get_item(Key={'transaction_type': transaction_type})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']
