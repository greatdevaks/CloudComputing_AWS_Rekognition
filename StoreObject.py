import boto3

# Creating Amazon S3 Client
s3 = boto3.resource("s3")

#Creating Amazon s3 Bucket
s3.create_bucket(Bucket = "bucketaksthree")

#Stroing object in bucket
s3.Object("bucketaksthree", "1.jpg").put(Body=open("Test/1.jpg", "rb"))
s3.Object("bucketaksthree", "2.jpg").put(Body=open("Test/2.jpg", "rb"))