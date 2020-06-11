from django.shortcuts import render
from  qr_app.models import *
import pdb

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
    return render(request, 'user_app/visitortLogin.html')

