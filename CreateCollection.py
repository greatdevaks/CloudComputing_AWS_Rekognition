import boto3

# Creating boto3 client
rekognition = boto3.client("rekognition", "us-east-1")

# Creting the collection for images
response = rekognition.create_collection(
    CollectionId="collectionOfFaces"
)

print(response)
