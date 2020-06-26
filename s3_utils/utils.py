import os
import boto3
from typing import Any

from . import exceptions


class S3Utils:

  def __init__(self):
    try:
      aws_profile = os.getenv('AWS_PROFILE_NAME')
      session = boto3.Session(profile_name=aws_profile)
      self._s3 = session.resource('s3')
      if os.getenv('S3_BUCKET_NAME'):
        self._default_bucket = self._s3.Bucket(os.getenv('S3_BUCKET_NAME'))
      self._default_bucket_name = os.getenv('S3_BUCKET_NAME')
    except Exception as e:
      raise exceptions.SessionInitException


  def set_default_bucket(self, bucket_name: str):
    if bucket_name is None:
      raise ValueError('bucket_name cannot be none.')
    if not isinstance(bucket_name, str):
      raise TypeError('bucket_name must be a string')
    if len(bucket_name) == 0:
      raise ValueError('bucket_name cannot be empty')
    self._default_bucket = self._s3.Bucket(bucket_name)
    self._default_bucket_name = bucket_name

  def move_object(self, old_key: str, new_key: str, bucket_name: str = None) -> bool:
    try:
      bucket_name = bucket_name if bucket_name is not None else self._default_bucket_name
      self._s3.Object(bucket_name, new_key).copy_from(
        CopySource=f"{bucket_name}/{old_key}")
      self._s3.Object(bucket_name, old_key).delete()
    except Exception as e:
      raise exceptions.MoveObjectException

  def copy_object(self, new_obj_key: str, src_obj_key: str, bucket_name: str = None):
    try:
      bucket_name = bucket_name if bucket_name is not None else self._default_bucket_name
      self._s3.Object(bucket_name, new_obj_key).copy_from(
        CopySource=f'{bucket_name}/{src_obj_key}')
    except Exception as e:
      raise exceptions.CopyObjectException

  def create_object(self, key: str, content: Any, bucket_name: str = None):
    try:
      bucket_name = bucket_name if bucket_name is not None else self._default_bucket_name
      s3_object = self._s3.Object(bucket_name, key)
      s3_object.put(Body=bytes(content, 'utf-8'))
    except Exception as e:
      raise exceptions.CreateObjectException

  def upload_file(self, key: str, file_path: str, bucket_name: str = None):
    try:
      bucket = self._default_bucket
      if bucket_name:
        bucket = self._s3.Bucket(bucket_name)
      bucket.upload_file(file_path, key)
    except Exception as e:
      raise exceptions.UploadFileException

  def delete_object(self, key: str, bucket_name: str = None) -> bool:
    try:
      bucket = self._default_bucket
      if bucket_name:
        bucket = self._s3.Bucket(bucket_name)
      bucket.delete_objects(
        Delete={
          'Objects': [{'Key': key}]
        },
      )
      return True
    except Exception as e:
      raise exceptions.DeleteObjectException

  def delete_objects(self, keys: list, bucket_name: str = None) -> bool:
    try:
      bucket = self._default_bucket
      if bucket_name:
        bucket = self._s3.Bucket(bucket_name)
      bucket.delete_objects(
        Delete={
          'Objects': [{'Key': key} for key in keys]
        },
      )
    except Exception as e:
      raise exceptions.DeleteObjectException

  def find_files_with_prefix(self, prefix: str, bucket_name: str = None) -> list:
    try:
      bucket = self._default_bucket
      if bucket_name:
        bucket = self._s3.Bucket(bucket_name)
      objects = bucket.objects.filter(
          Prefix=prefix
      )
      return objects
    except Exception as e:
      raise exceptions.DirectoryReadException
