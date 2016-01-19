##

import boto3


s3 = boto3.resource('s3')

# Print out bucket files and print the first line of the first one bucket files
#   and print the first line of the first one.
bucket = s3.Bucket('mya-d3-prd-report')
for f in bucket.objects.all():
    print (f)


