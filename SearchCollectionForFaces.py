import boto3

# Creating boto3 client
rekognition = boto3.client("rekognition", "us-east-1")

collection_name = "collectionOfFaces"
bucket_name = "bucketaksthree"
photo_to_be_uploaded = "Test/2.jpg".split("/")[-1]
image_id = photo_to_be_uploaded.split(".")[0].split("/")[-1]

response = rekognition.search_faces_by_image(
    CollectionId=collection_name,
    FaceMatchThreshold=75,
    Image={
        'S3Object': {
            'Bucket': bucket_name,
            'Name': photo_to_be_uploaded,
        },
    },
    MaxFaces=5,
)

if(response['FaceMatches']):
    for elements in response['FaceMatches']:
        print(elements['Face']['FaceId'])
        print(elements['Face']['ImageId'])
        print("Image Faces/" + elements['Face']['ExternalImageId'] + ".jpg matched.")
else:
    print("No match found.")
