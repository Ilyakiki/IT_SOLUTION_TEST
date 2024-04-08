from django.shortcuts import render
import cv2
import numpy as np
import os
import mimetypes
from .video import create_video
from django.http.response import HttpResponse
from .models import Request

# Create your views here.
def home(request):
    return render(request,'video_maker/home.html')


def video(request):

    message=request.GET["message"]

    create_video(message)
    Request(message=message).save()

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_name=f'/ready_video.mp4'
    mime_type, _ = mimetypes.guess_type(BASE_DIR + file_name)
    with open(BASE_DIR + f'/ready_video.mp4', 'rb') as p:
        response = HttpResponse(p, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % file_name
    return response
