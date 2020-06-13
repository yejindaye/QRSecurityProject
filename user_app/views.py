from django.shortcuts import render
from  qr_app.models import *
import pdb
from random import *
from .models import QrAppResident
from .models import QrAppVisitor
from .models import QrAppApartment

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

# 회원가입
def residentSignUp(request):
    if request.method == "POST":
        pdb.set_trace()
        uid = request.POST.get('uid')
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        birth_year = request.POST.get('birth_year')
        building_num = request.POST.get('building')
        floor_num = request.POST.get('floor')
        room_num = request.POST.get('room')
        building = Building.objects.create(number = building_num)
        floor = Building.objects.create(number = floor_num)
        room = Building.objects.create(number = room_num)
        apt = Apartment.objects.create(building = building, floor = floor, room = room)
        #apt완성
        resident = Resident.objects.create(uid = uid, pw = pw, name = name, birth_year = birth_year, room = apt)
        return redirect('qrDisplay')
    return render(request, 'user_app/residentSignUp.html')


def visitorSignUp(request):
    return render(request, 'user_app/visitorSignUp.html');    


# 로그인
def residentLogin(request):
    # request.user_agent.is_mobile # returns True
    # request.user_agent.is_tablet # returns False
    # request.user_agent.is_touch_capable # returns True
    # request.user_agent.is_pc # returns False
    # request.user_agent.is_bot # returns False
    # os = request.user_agent.os
    # print(os)
    return render(request, 'user_app/residentLogin.html')

def visitorLogin(request):
    return render(request, 'user_app/visitorLogin.html')

#방문자 회원가입 디비저장
def doVisitorSignUp(request):
    if request.method=='POST':
        id=request.POST['id']
        pw=request.POST['pw']
        name=request.POST['name']
        birth_year=request.POST['birth_year']
        rand_salt=randrange(1000000)
        new_visitor=QrAppVisitor(uid=id,pw=pw, name=name, birth_year=birth_year,salt=rand_salt)
        new_visitor.save()
    return render(request, 'index.html')

#세대원 회원가입 디비저장
def doResidentSignUp(request):
    if request.method=='POST':
        id=request.POST['id']
        pw=request.POST['pw']
        name=request.POST['name']
        birth_year=request.POST['birth_year']
        dong=request.POST['dong']
        ho=request.POST['ho']
        floor=request.POST['floor']
        rand_salt=randrange(1000000)
        new_visitor=QrAppResident(uid=id,pw=pw, name=name, birth_year=birth_year,salt=rand_salt)
        new_visitor.save()
        new_apartment=QrAppApartment(uid=id,building_id=dong, room_id=ho,floor_id=floor)
        new_apartment.save()

    return render(request, 'index.html')