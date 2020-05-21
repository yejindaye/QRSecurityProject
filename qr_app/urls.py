from django.urls import path, include
from . import views
urlpatterns = [
    path('visitorLogin/', views.visitorLogin, name = "visitorLogin"),
    path('householdLogin/', views.householdLogin, name = "householdLogin"),
    path('qrDisplay/', views.qrDisplay, name = "qrDisplay"),
]