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

## Examples
### ```set_default_bucket```
Sets the default bucket for *s3-related* operations. Usage:
```
s3.set_default_bucket('bucket_name')
```

### ```move_object```
Assigns a new key to the object inside a bucket. The process involves creating a new object, copy the old object to new object, and delete old object. Usage:
```
s3.move_object('directory/unprocessed/file.json', 'directory/processed/file.json')
```

If you want to peform this operation on a bucket other than default, use:
```
s3.move_object('directory/unprocessed/file.json', 'directory/processed/file.json', 'bucket_name')
```

### ```copy_object```
Assigns a new key to the object inside a bucket. The process involves creating a new object, copy the old object to new object, and delete old object. Usage:
```
s3.copy_object('new_object_key', 'src_object_key')
```

If you want to peform this operation on a bucket other than default, use:
```
s3.copy_object('new_object_key', 'src_object_key', 'bucket_name')
```

### ```create_object```
Creates a new object inside a bucket and sets its content/body. The process involves creating a new object, copy the old object to new object, and delete old object. Usage:
```
import json
data = {
  'message': 'Hello world',
  'created_at': '2020-06-03 05:36:00'
}
formatted_data = json.dumps(data)
s3.create_object('key', formatted_data)
```

If you want to peform this operation on a bucket other than default, use:
```
s3.create_object('key', formatted_data, 'bucket_name')
```

### ```upload_file```
Uploads a file on disk storage as an object on S3. Usage:
```
file_path = os.path.join('/tmp', 'unprocessed', 'response.json')
s3.upload_file('file_key', file_path)
```

If you want to peform this operation on a bucket other than default, use:
```
file_path = os.path.join('/tmp', 'unprocessed', 'response.json')
s3.upload_file('file_key', file_path, 'bucket_name')
```

### ```delete_object```
Deletes an object from a bucket on S3. Usage:
```
s3.delete_object('key')
```

If you want to peform this operation on a bucket other than default, use:
```
s3.delete_object('key', 'bucket_name')
```

### ```delete_objects```
Deletes objects matching the supplied keys from a bucket. Usage:
```
s3.delete_objects(['key1, key2', 'key3'])
```

If you want to peform this operation on a bucket other than default, use:
```
s3.delete_objects(['key1, key2', 'key3'], 'bucket_name')
```

### ```find_files_with_prefix```
Finds files/objects matching the given prefix. This is helpful if you want to get objects in a specific (hypothetical) directory. Usage:
```
s3.find_files_with_prefix('/organization/unprocessed/prefix')
```

If you want to peform this operation on a bucket other than default, use:
```
s3.find_files_with_prefix('/organization/unprocessed/prefix', 'bucket_name')
```
