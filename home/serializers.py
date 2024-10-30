import shutil
from rest_framework import serializers
from .models import *

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField(max_length=10000, allow_empty_file=False, use_url=False)
    )
    folder = serializers.CharField(required=False)

    def zip(self, folder_uid):
        # Make sure to create a zip file correctly
        shutil.make_archive(f"public/static/zip/{folder_uid}", "zip", f'public/static/zip/{folder_uid}')

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop("files")
        files_obj = []

        for file in files:
            file_obj = File.objects.create(folder=folder, file=file)
            files_obj.append(file_obj)

        # Create the zip file with the folder's uid
        self.zip(folder.uid)

        # Return the folder UID for further use
        return {
            "files": {},
            "folder": str(folder.uid)  # Return the string representation of the folder UID
        }