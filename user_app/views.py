from django.shortcuts import render, redirect
from  qr_app.models import *
import pdb
from random import *
from .models import QrAppResident
from .models import QrAppVisitor
from .models import QrAppApartment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


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

# 로그인
def residentLogin(request):
    # request.user_agent.is_mobile # returns True
    # request.user_agent.is_tablet # returns False
    # request.user_agent.is_touch_capable # returns True
    # request.user_agent.is_pc # returns False
    # request.user_agent.is_bot # returns False
    # os = request.user_agent.os
    # print(os)
    if request.method == 'POST':
        uid = request.POST['id']
        pw = request.POST['pw']
        if QrAppResident.objects.filter(uid = uid, pw = pw):
            return redirect('resAfterLogin')
        messages.info(request, '없는 계정이거나 비밀번호가 일치하지 않습니다.')    
        return render(request, 'user_app/residentLogin.html')
    return render(request, 'user_app/residentLogin.html')




def visitorLogin(request):
    if request.method == 'POST':
        uid = request.POST['id']
        pw = request.POST['pw']
        if QrAppVisitor.objects.filter(uid = uid, pw = pw):
            return redirect('visAfterLogin')
        messages.info(request, '없는 계정이거나 비밀번호가 일치하지 않습니다.')    
        return render(request, 'user_app/visitorLogin.html')
    return render(request, 'user_app/visitorLogin.html')
    

#방문자 회원가입 디비저장
def visitorSignUp(request):
    if request.method=='POST':
        id=request.POST['id']
        pw=request.POST['pw']
        name=request.POST['name']
        birth_year=request.POST['birth_year']
        rand_salt=randrange(1000000)
        new_visitor=QrAppVisitor(uid=id,pw=pw, name=name, birth_year=birth_year,salt=rand_salt)
        new_visitor.save()
        return redirect('visAfterLogin')
    return render(request, 'user_app/visitorSignUp.html');    

#세대원 회원가입 디비저장
def residentSignUp(request):
    if request.method=='POST':
        id=request.POST['id']
        pw=request.POST['pw']
        name=request.POST['name']
        birth_year=request.POST['birth_year']
        dong=request.POST['dong']
        ho=request.POST['ho']
        floor=request.POST['floor']
        rand_salt=randrange(1000000)
        apt =  QrAppApartment.objects.create(uid)
        post = Post.objects.create(user = user, title = title, content = content, image = image, category = category, amount = amount, cooking_time = cooking_time, cooking_level = cooking_level)
        # 아파트 완성
        new_resident = QrAppResident.objects.create(uid=id,pw=pw, name=name, birth_year=birth_year,salt=rand_salt)
        new_resident.save()
        new_apartment=QrAppApartment(uid=id,building_id=dong, room_id=ho,floor_id=floor)
        new_apartment.save()
        return redirect('resAfterLogin')
    return render(request, 'user_app/residentSignUp.html');             
