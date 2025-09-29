import boto3

sagemaker = boto3.client('sagemaker')
endpoint_name = "your-endpoint-name"  # Replace with your actual name

# Delete the endpoint
sagemaker.delete_endpoint(EndpointName=endpoint_name)
print("🧹 Endpoint deleted:", endpoint_name)

# Delete the endpoint configuration
sagemaker.delete_endpoint_config(EndpointConfigName=endpoint_name)
print("🧹 Endpoint config deleted:", endpoint_name)