import os
import json
import http.client

def lambda_handler(event, context):
    
    dapnetHost = os.environ['DAPNET_HOST']
    dapnetAuthHeader = os.environ['DAPNET_AUTH_HEADER']
    dapnetPath = os.environ['DAPNET_PATH']
  
    body = json.loads(event['body'])
    body_dic = json.loads(body)
    
    callSignNames = body_dic['callSignNames']
    transmitterGroupNames = body_dic['transmitterGroupNames']
    message = body_dic['message']
        
    conn = http.client.HTTPSConnection(dapnetHost)

    payload = json.dumps({
      "text": message,
      "callSignNames": callSignNames,
      "transmitterGroupNames": transmitterGroupNames,
      "emergency": False
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': dapnetAuthHeader
    }
    conn.request("POST", dapnetPath, payload, headers)
    res = conn.getresponse()
    data = res.read()
   
    return {
        'statusCode': res.status,
        'body': json.dumps(data.decode("utf-8"))
    }
    

