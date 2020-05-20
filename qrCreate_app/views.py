from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

import qrcode
import cv2
# Create your views here.

def index(request):
    #faqs = Faq.objects.all()
    #context={'faqs':faqs}
    img = qrcode.make("Hello World!")
    img.save("qrCreate_app/static/qrCreate_app/images/helloworld_qrcode.png")

    return render(request,'./qr.html',)
