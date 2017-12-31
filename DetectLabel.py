import boto3

#Creating Amazon S3 Client
s3 = boto3.resource("s3")

#Creating Amazon s3 Bucket
s3.create_bucket(Bucket = "bucketakstwo")

# #Stroing object in bucket

s3.Object("bucketakstwo", "butterfly.jpg").put(Body=open("butterfly.jpg", "rb"))

#Printing the buckets
for bucket in s3.buckets.all():
    print(bucket.objects.all())
    for key in bucket.objects.all():
        print(key.key)

BUCKET = "bucketakstwo"
KEY = "butterfly.jpg"

def detect_labels(bucket, key, max_labels=10, min_confidence=90, region="us-east-1"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.detect_labels(
		Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		MaxLabels=max_labels,
		MinConfidence=min_confidence,
	)
	return response['Labels']

detect_labels(BUCKET,KEY)
for label in detect_labels(BUCKET, KEY):
	print("{Name} - {Confidence}%".format(**label))
