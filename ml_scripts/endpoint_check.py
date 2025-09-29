import boto3

sm = boto3.client('sagemaker')
endpoint_name = "your-endpoint-name"

try:
    response = sm.describe_endpoint(EndpointName=endpoint_name)
    print("✅ Endpoint status:", response['EndpointStatus'])
except:
    print("❌ Endpoint not found. You’ll need to redeploy.")