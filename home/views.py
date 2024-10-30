from django.shortcuts import render
from rest_framework.views import APIView
from home.serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from rest_framework.parsers import MultiPartParser

# Create your views here.

class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        serializers = FileListSerializer(data=request.data)
        if serializers.is_valid():
            # Call create method to get the created folder data
            folder_data = serializers.create(serializers.validated_data)
            folder_id = folder_data.get("folder")  # Get the folder ID
            print(folder_id)  # Now you can access the folder ID here

            return Response({
                "msg": "file uploaded success",
                "folder": folder_id  # You can also return the folder ID if needed
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors)


class home(View):
    def get(self, request):
        return render(request, "home.html")
    

def download(request,uid):
        return render(request, "download.html",context={"uid":uid})
    

        