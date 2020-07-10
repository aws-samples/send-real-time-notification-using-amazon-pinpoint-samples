import boto3
from botocore.exceptions import ClientError
def sendEmail(AWS_REGION,SENDER,TOADDRESS,APPID,SUBJECT,BODY_TEXT,BODY_HTML,CHARSET):
    
    AWS_REGION = AWS_REGION
    SENDER = SENDER
    
    # The addresses on the "To" line. If your Amazon Pinpoint account is in
    # the sandbox, these addresses also have to be verified.
    TOADDRESS = TOADDRESS
    
    # The Amazon Pinpoint project/application ID to use when you send this message.
    # Make sure that the email channel is enabled for the project or application
    # that you choose.
    APPID = APPID
    
    # The subject line of the email.
    SUBJECT = SUBJECT
    
    # The body of the email for recipients whose email clients don't support HTML
    # content.
    BODY_TEXT = BODY_TEXT
    
    # The body of the email for recipients whose email clients can display HTML
    # content.
    BODY_HTML = BODY_HTML 
    

    CHARSET = CHARSET
    
    # Create a new client and specify a region.
    client = boto3.client('pinpoint',region_name=AWS_REGION)
    try:
        response = client.send_messages(
            ApplicationId=APPID,
            MessageRequest={
                'Addresses': {
                    TOADDRESS: {
                         'ChannelType': 'EMAIL'
                    }
                },
                'MessageConfiguration': {
                    'EmailMessage': {
                        'FromAddress': SENDER,
                        'SimpleEmail': {
                            'Subject': {
                                'Charset': CHARSET,
                                'Data': SUBJECT
                            },
                            'HtmlPart': {
                                'Charset': CHARSET,
                                'Data': BODY_HTML
                            },
                            'TextPart': {
                                'Charset': CHARSET,
                                'Data': BODY_TEXT
                            }
                        }
                    }
                }
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return("Error")
    else:
        print( response['MessageResponse'])
        return("Success")
