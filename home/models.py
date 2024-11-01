from django.db import models
import uuid
import os 

# Create your models here.

class Folder(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at = models.DateField(auto_now=True)


def get_upload_path(object,filename):
    return os.path.join(str(object.folder.uid), filename)
                            # file.Folder.uid



class File(models.Model):
    folder = models.ForeignKey(Folder,on_delete= models.CASCADE, related_name="files")
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateField(auto_now=True)
