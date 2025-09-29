import boto3

sm = boto3.client('sagemaker')
response = sm.list_endpoints(SortBy='CreationTime', SortOrder='Descending')

for ep in response['Endpoints']:
    print(f"Name: {ep['EndpointName']} | Status: {ep['EndpointStatus']}")