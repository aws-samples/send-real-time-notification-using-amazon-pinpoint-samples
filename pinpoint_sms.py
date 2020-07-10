# -*- coding: utf-8 -*-

import boto3
from botocore.exceptions import ClientError

def sendSMS(region,originationNumber,destinationNumber,message,applicationId,messageType,registeredKeyword,senderId):

    region = region
    originationNumber = originationNumber
    destinationNumber = destinationNumber
    message = message
    applicationId = applicationId
    messageType = messageType
    registeredKeyword = registeredKeyword

    senderId = senderId
    
    # Create a new client and specify a region.
    client = boto3.client('pinpoint',region_name=region)
    try:
        response = client.send_messages(
            ApplicationId=applicationId,
            MessageRequest={
                'Addresses': {
                    destinationNumber: {
                        'ChannelType': 'SMS'
                    }
                },
                'MessageConfiguration': {
                    'SMSMessage': {
                        'Body': message,
                        'Keyword': registeredKeyword,
                        'MessageType': messageType,
                        'OriginationNumber': originationNumber,
                        'SenderId': senderId
                    }
                }
            }
        )
    
    except ClientError as e:
        print("error")
        print(e.response['Error']['Message'])
        return("Error")
    else:
        print(response['MessageResponse']['Result'][destinationNumber]['MessageId'])
        return("Sucecss")
