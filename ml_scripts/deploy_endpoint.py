from sagemaker import image_uris
from sagemaker.model import Model
from sagemaker import get_execution_role

role = get_execution_role()

image_uri = image_uris.retrieve(
    framework="xgboost",
    region="eu-west-1",
    version="1.3-1"
)

model_uri = "s3://your-s3-bucket-name/naija-sentiment/model.tar.gz"

model = Model(
    image_uri=image_uri,
    model_data=model_uri,
    role=role,
    entry_point="inference.py"
)

predictor = model.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large"
)

print("🚀 Endpoint deployed:", predictor.endpoint_name)