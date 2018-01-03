import boto3

# Creating boto3 client
rekognition = boto3.client("rekognition", "us-east-1")

collection_name = "collectionOfFaces"
bucket_name = "bucketakstwo"
photo_to_be_uploaded = "Faces/6.jpg".split("/")[-1]
image_id = photo_to_be_uploaded.split(".")[0].split("/")[-1]

response = rekognition.index_faces(
    CollectionId=collection_name,
    DetectionAttributes=[
        "ALL", "DEFAULT"
    ],
    ExternalImageId=image_id,
    Image={
        'S3Object': {
            'Bucket': bucket_name,
            'Name': photo_to_be_uploaded,
        },
    },
)

print(response)
