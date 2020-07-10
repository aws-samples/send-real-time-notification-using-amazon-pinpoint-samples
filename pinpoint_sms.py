"""
This module is used to send SMS using Amazon Pinpoint to specified mobile

region  : The AWS Region that you want to use to send the email. For a list of AWS Regions where the 
          Amazon Pinpoint API is available, see https://docs.aws.amazon.com/pinpoint/latest/apireference/
          
origination_number : The phone number or short code to send the message from. The phone number or short code 
                     that you specify has to be associated with your Amazon Pinpoint account. For best results, 
                     specify long codes in E.164 format.
                     
destination_number : The recipient's phone number.  For best results, you should specify the phone number in E.164 format.

message : The content of the SMS message.

application_id  : The Amazon Pinpoint project/application ID to use when you send this message.
                  Make sure that the email channel is enabled for the project or application that you choose.
                  
message_type : The type of SMS message that you want to send. If you plan to send time-sensitive content, 
               specify TRANSACTIONAL. If you plan to send marketing-related content, specify PROMOTIONAL.
               
registered_keyword : The registered keyword associated with the originating short code

sender_id :  The sender ID to use when sending the message. Support for sender ID varies by country or region. 
            For more information, see  https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-countries.html
"""
import boto3
from botocore.exceptions import ClientError

def sendSMS(region,origination_number,destination_number,message,application_id,message_type,registered_keyword,sender_id):

    
    # Create a new client and specify a region.
    client = boto3.client('pinpoint',region_name=region)
    try:
        response = client.send_messages(
            ApplicationId=application_id,
            MessageRequest={
                'Addresses': {
                    destination_number: {
                        'ChannelType': 'SMS'
                    }
                },
                'MessageConfiguration': {
                    'SMSMessage': {
                        'Body': message,
                        'Keyword': registered_keyword,
                        'MessageType': message_type,
                        'OriginationNumber': origination_number,
                        'SenderId': sender_id
                    }
                }
            }
        )
    
    except ClientError as e:
        print("error")
        print(e.response['Error']['Message'])
        return("Error")
    else:
        print(response['MessageResponse']['Result'][destination_number]['MessageId'])
        return("Success")
