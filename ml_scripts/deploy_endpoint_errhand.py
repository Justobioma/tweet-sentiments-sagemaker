from sagemaker import image_uris
from sagemaker.model import Model
from sagemaker import get_execution_role
import traceback

role = get_execution_role()

image_uri = image_uris.retrieve(
    framework="xgboost",
    region="eu-west-1",
    version="1.3-1"
)

model_uri = "s3://your-s3-bucket-name/naija-sentiment/model.tar.gz"  # Update this

model = Model(
    image_uri=image_uri,
    model_data=model_uri,
    role=role,
    entry_point="inference.py"
)

try:
    predictor = model.deploy(
        initial_instance_count=1,
        instance_type="ml.m5.large",
        endpoint_name="obioma-sentiment-v1"  # Optional: set a custom name
    )
    print("🚀 Endpoint deployed successfully!")
    print("Endpoint name:", predictor.endpoint_name)
except Exception as e:
    print("❌ Deployment failed.")
    traceback.print_exc()
    predictor = None