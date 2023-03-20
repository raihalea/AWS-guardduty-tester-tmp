import json
import socket

def lambda_handler(event, context):

    domain = "guarddutyc2activityb.com"
    result = socket.gethostbyname(domain)

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }