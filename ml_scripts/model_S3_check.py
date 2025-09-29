import boto3

s3 = boto3.client('s3')
bucket_name = "your-s3-bucket-name"
s3_key = "naija-sentiment/model.tar.gz"

# Check if the file exists
try:
    s3.head_object(Bucket=bucket_name, Key=s3_key)
    print("✅ Model artifact is still in S3.")
except:
    print("❌ Model artifact not found. You may need to re-upload.")