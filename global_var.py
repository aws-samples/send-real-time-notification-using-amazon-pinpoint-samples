"""
This is global module to assign the value of variables which is not coming from DynamoDB
"""
# The Amazon Pinpoint project/application ID to use when you send this message.
# Make sure that the SMS channel is enabled for the project or application
# that you choose.
application_id = ""

# The type of SMS message that you want to send. If you plan to send
# time-sensitive content, specify TRANSACTIONAL. If you plan to send
# marketing-related content, specify PROMOTIONAL.
message_type = "TRANSACTIONAL"

# The registered keyword associated with the originating short code.
registered_keyword = "myKeyword"

sender_id = "Mysender_id"

# The AWS Region that you want to use to send the message. For a list of
# AWS Regions where the Amazon Pinpoint API is available, see
# https://docs.aws.amazon.com/pinpoint/latest/apireference/
region = ""

# The phone number or short code to send the message from. The phone number
# or short code that you specify has to be associated with your Amazon Pinpoint
# account. For best results, specify long codes in E.164 format.
origination_number = ""


# The "From" address. This address has to be verified in
# Amazon Pinpoint in the region you're using to send email.
sender = ""

# The character encoding that you want to use for the subject line and message
# body of the email.  
charset = "UTF-8"
