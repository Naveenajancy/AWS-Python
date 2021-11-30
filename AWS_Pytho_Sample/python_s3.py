# Create S3 bucket , list and  delete objects and buckets
import uuid
import boto3
#connect client
s3client = boto3.client('s3')

#create bucket
bucket_name = 'kkktest-{}'.format(uuid.uuid4())
print('Creating new s3 bucket :{}'.format(bucket_name))
s3client.create_bucket(Bucket=bucket_name)

#List buckets
list_bucket_resp = s3client.list_buckets()
for bucket in list_bucket_resp['Buckets']:
    #print(bucket['Name'])
    print('(created) --> {} - there since {}'.format(
        bucket['Name'], bucket['CreationDate']))

#put / get objects
object_key = "sample_key.txt"
s3client.put_object(Bucket=bucket_name, Key=object_key, Body=b'my_sample_file')

url = s3client.generate_presigned_url(
    'get_object', {'Bucket': bucket_name, 'Key': object_key})
print('\nTry this URL in your browser to download the object:')
print(url)

s3resource = boto3.resource('s3')
bucket = s3resource.Bucket(bucket_name)
obj = bucket.Object(object_key)
print('Bucket name: {}'.format(bucket.name))
print('Object key: {}'.format(obj.key))
print('Object content length: {}'.format(obj.content_length))
print('Object body: {}'.format(obj.get()['Body'].read()))
print('Object last modified: {}'.format(obj.last_modified))

# Buckets cannot be deleted unless they're empty. Let's keep using the
# Resource API to delete everything. Here, we'll utilize the collection
# 'objects' and its batch action 'delete'. Batch actions return a list
# of responses, because boto3 may have to take multiple actions iteratively to
# complete the action.

for bucketinfo in list_bucket_resp['Buckets']:
    uniquebucketName = bucketinfo['Name']
    uniquebucket = s3resource.Bucket(uniquebucketName)
    print('\nDeleting all objects in bucket {}.'.format(uniquebucketName))
    delete_responses = uniquebucket.objects.delete()
    for delete_response in delete_responses:
        for deleted in delete_response['Deleted']:
            print('\t Deleted: {}'.format(deleted['Key']))

    #delete bucket
    print('\n Deleting the bucket ..')
    uniquebucket.delete()

