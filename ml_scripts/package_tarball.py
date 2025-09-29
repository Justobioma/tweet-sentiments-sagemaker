import tarfile

with tarfile.open("model.tar.gz", "w:gz") as tar:
    tar.add("model_bundle.pkl", arcname="model_bundle.pkl")
    tar.add("inference.py", arcname="inference.py")

