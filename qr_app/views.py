from django.shortcuts import render,redirect, get_object_or_404

# Create your views here.
def visitorLogin(request):
    return render(request, 'qr_app/visitorLogin.html')

def householdLogin(request):
    return render(request, 'qr_app/householdLogin.html')