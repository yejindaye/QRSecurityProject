from django.urls import path, include
from . import views
urlpatterns = [
    path('qrDisplay/', views.qrDisplay, name = "qrDisplay"),
]