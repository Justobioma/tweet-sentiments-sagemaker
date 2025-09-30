import boto3

runtime = boto3.client('sagemaker-runtime')

response = runtime.invoke_endpoint(
    EndpointName="obioma-sentiment-v1",
    ContentType="text/csv",
    Body="Naija youths dey hustle pass their parents"
)

result = response['Body'].read().decode('utf-8')
print("🧠 Human-Friendly Prediction:", result)