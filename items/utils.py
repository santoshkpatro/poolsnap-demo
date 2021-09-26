import shortuuid
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def handle_local_upload(f):
    ext = f.content_type.split('/')[1]
    filename = shortuuid.uuid() + '.' + ext
    fs = FileSystemStorage()
    file_name = fs.save(filename, f)
    file_url = fs.url(file_name)
    return file_url
