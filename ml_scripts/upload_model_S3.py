import boto3

s3 = boto3.client('s3')
bucket_name = "your-s3-bucket-name"
s3_key = "naija-sentiment/model.tar.gz"

s3.upload_file("model.tar.gz", bucket_name, s3_key)
model_uri = f"s3://{bucket_name}/{s3_key}"
print("✅ Model re-uploaded to:", model_uri)