"""
This module sends email using Amazon Pinpoint to specified recipients

aws_region : The AWS Region that you want to use to send the email. For a list of AWS Regions where the 
             Amazon Pinpoint API is available, see https://docs.aws.amazon.com/pinpoint/latest/apireference/

sender :   The "From" address. This address has to be verified in Amazon Pinpoint in the region 
           you're using to send email.

to_address : The addresses on the "To" line. If your Amazon Pinpoint account is in the sandbox, 
            these addresses also have to be verified
            
app_id : The Amazon Pinpoint project/application ID to use when you send this message.
        Make sure that the email channel is enabled for the project or application that you choose.
        
subject : The subject line of the email.

body_text : The body of the email for recipients whose email clients don't support HTML content.

body_html : The body of the email for recipients whose email clients can display HTML content

charset : The character encoding that you want to use for the subject line and message body of the email

"""
import boto3
from botocore.exceptions import ClientError
def sendEmail(aws_region,sender,to_address,app_id,subject,body_text,body_html,charset):
            
    # Create a new client and specify a region.
    client = boto3.client('pinpoint',region_name=aws_region)
    try:
        response = client.send_messages(
            ApplicationId=app_id,
            MessageRequest={
                'Addresses': {
                    to_address: {
                         'ChannelType': 'EMAIL'
                    }
                },
                'MessageConfiguration': {
                    'EmailMessage': {
                        'FromAddress': sender,
                        'SimpleEmail': {
                            'Subject': {
                                'Charset': charset,
                                'Data': subject
                            },
                            'HtmlPart': {
                                'Charset': charset,
                                'Data': body_html
                            },
                            'TextPart': {
                                'Charset': charset,
                                'Data': body_text
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
