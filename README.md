# s3-wrapper
**s3-wrapper** is a wrapper around *s3-related* functionalities of AWS's **boto3** package.

## Quick Start
First, install the library:
```
pip install s3-wrapper
```
Next, set up credentials (in e.g. ```~/.aws/credentials```):
```
[default]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET
```
You should set the following values in environment variables:
1. **AWS_PROFILE_NAME**: AWS profile name
2. **S3_BUCKET_NAME** (Optional): Default bucket name

If **S3_BUCKET_NAME** is not found in environment variables, you must set the default directory before using any utilities:
```
s3 = S3Utils()
s3.set_default_bucket('test_bucket')
```

You can use [python-dotenv](https://pypi.org/project/python-dotenv/) for loading environment variables.