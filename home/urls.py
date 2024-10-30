from django.urls import path
from .views import *


urlpatterns = [

    path("", HandleFileUpload.as_view(), name= "file-handle"),
    path("home", home.as_view(), name= "home"),
    path("download/<uid>/", download, name= "download"),
]