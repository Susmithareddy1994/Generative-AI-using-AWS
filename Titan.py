import boto3
import json

prompt_data="""
Write about the nachine learning Algorithms
"""

bedrock = boto3.client(service_name = 'bedrock-runtime')

body=json.dumps({
    "inputText": prompt_data,
    "textGenerationConfig":{
        "maxTokenCount": 1024,
        "stopSequences": [],
        "temperature": 0,
        "topP": 0.9
    }
}) 
response = bedrock.invoke_model(

    body=body,
        modelId="amazon.titan-text-premier-v1:0",
    accept="application/json",
    contentType="application/json"
)
response_body=json.loads(response.get('body').read())
print(response_body.get('results')[0].get('outputText'))