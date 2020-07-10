from __future__ import print_function
from pinpoint_sms import *
from pinpoint_email import *
from read_rule_table import *  
from global_var import *
from decimal import Decimal

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            if record['eventName'] == 'INSERT':
                handle_insert(record)
    except Exception as e:
        print(e)
        
def handle_insert(record):
    newImage = record['dynamodb']['NewImage']
    order_id = newImage['order_id']['S']
    customer_name = newImage['customer_name']['S']
    order_date = newImage['order_date']['S']
    order_value = newImage['order_value']['N']
    order_value_unit = newImage['unit']['S']
    delivery_date = newImage['delivery_date']['S']
   
   #get transaction_alert_rule table to fetch high value transaction threshold
    premium_item = get_premium_rule("premium",)
    send_notification = premium_item['send_notification']
    min_transaction_value = premium_item['min_transaction_value']
    to_address = premium_item['email']
    destination_number = premium_item['phone']
    unit = premium_item['unit']
    print(send_notification)
    
    #Check high order value transaction 
    if (float(order_value) >= float(min_transaction_value)) and (send_notification == True) and (order_value_unit == unit):
        message = ("Customer " + customer_name  + " has created an order of value " +  order_value + unit + ".Please check Order " + order_id +" for details")
        send_sms_status = sendSMS(region,origination_number,destination_number,message,application_id,message_type,registered_keyword,sender_id)
        
        subject = " High value transaction"
        body_text = "Transaction details : "
        body_html = "Customer " + customer_name  + " has created an order of value " +  order_value + unit+ ".Please check Order " + order_id +" for details"
        send_email_status = sendEmail(region,sender,to_address,application_id,subject,body_text,body_html,charset)
