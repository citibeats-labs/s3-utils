class SessionInitException(Exception):
  """
  Should be raised when s3 session fails to initialize
  """
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
  
  def __str__(self):
    if self.message:
      return f'SessionInitException, {self.message}'
    else:
      return 'SessionInitException: Failed to init session'


class DirectoryReadException(Exception):
  """
  Should be raised when storage handler fails to read a directory
  """
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
  
  def __str__(self):
    if self.message:
      return f'DirectoryReadException, {self.message}'
    else:
      return 'DirectoryReadException: Failed to read directory'


class MoveObjectException(Exception):
  """
  Should be raised when s3 fails to move an object
  """
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
  
  def __str__(self):
    if self.message:
      return f'MoveObjectException, {self.message}'
    else:
      return 'MoveObjectException: Failed to move object'


class CreateObjectException(Exception):
  """
  Should be raised when handler fails to create an object
  """
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
  
  def __str__(self):
    if self.message:
      return f'CreateObjectException, {self.message}'
    else:
      return 'CreateObjectException: Failed to create an object'


class UploadFileException(Exception):
  """
  Should be raised when handler fails to upload a file
  """
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
  
  def __str__(self):
    if self.message:
      return f'UploadFileException, {self.message}'
    else:
      return 'UploadFileException: Failed to upload a file'


class DeleteObjectException(Exception):
  """
  Should be raised when handler fails to delete an object
  """
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
  
  def __str__(self):
    if self.message:
      return f'DeleteObjectException, {self.message}'
    else:
      return 'DeleteObjectException: Failed to delete an object'


class CopyObjectException(Exception):
  """
  Should be raised when handler fails to copy an object
  """
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
  
  def __str__(self):
    if self.message:
      return f'CopyObjectException, {self.message}'
    else:
      return 'CopyObjectException: Failed to copy an object'


class PresignedUrlGenerationException(Exception):
  """
  Should be raised when handler to generate presigned-url.
  """
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
  
  def __str__(self):
    if self.message:
      return f'PresignedUrlGenerationException, {self.message}'
    else:
      return 'PresignedUrlGenerationException: Failed to generate presigned-url.'


class DownloadFileException(Exception):
  """
  Should be raised when handler fails to download a file.
  """
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
  
  def __str__(self):
    if self.message:
      return f'DownloadFileException, {self.message}'
    else:
      return 'DownloadFileException: Failed to download the file.'
