from django.shortcuts import render,redirect, get_object_or_404
# from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
# import qrcode
# import cv2

def visitorLogin(request):
    return render(request, 'user_app/residentLogin.html')

def householdLogin(request):
    # request.user_agent.is_mobile # returns True
    # request.user_agent.is_tablet # returns False
    # request.user_agent.is_touch_capable # returns True
    # request.user_agent.is_pc # returns False
    # request.user_agent.is_bot # returns False
    # os = request.user_agent.os
    # print(os)
    return render(request, 'user_app/residentLogin.html')

# def my_view(request):

#     # Let's assume that the visitor uses an iPhone...
#     request.user_agent.is_mobile # returns True
#     request.user_agent.is_tablet # returns False
#     request.user_agent.is_touch_capable # returns True -> 이거3개 이넘
#     request.user_agent.is_pc # returns False
#     request.user_agent.is_bot # returns False

#     # Accessing user agent's browser attributes
#     request.user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
#     request.user_agent.browser.family  # returns 'Mobile Safari'
#     request.user_agent.browser.version  # returns (5, 1)
#     request.user_agent.browser.version_string   # returns '5.1'

#     # Operating System properties
#     request.user_agent.os  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
#     request.user_agent.os.family  # returns 'iOS' ->이거
#     request.user_agent.os.version  # returns (5, 1)->이거
#     request.user_agent.os.version_string  # returns '5.1' -> 이거

#     # Device properties
#     request.user_agent.device  # returns Device(family='iPhone')
#     request.user_agent.device.family  # returns 'iPhone'

def createQR(request):
    #faqs = Faq.objects.all()
    #context={'faqs':faqs}
    img = qrcode.make("Hello World!")
    img.save("qrCreate_app/static/qrCreate_app/images/helloworld_qrcode.png")
    return render(request,'./qr.html',)


def qrDisplay(request):
    qrCode="Os info"

    return render(request, 'qr_app/qrDisplay.html',{'qrCode':qrCode})

