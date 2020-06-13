from django.urls import path, include
from . import views

urlpatterns = [
     path('residentSignUp/', views.residentSignUp, name = "residentSignUp"),
     path('visitorSignUp/', views.visitorSignUp, name = "visitorSignUp"),
     path('residentLogin/', views.residentLogin, name = "residentLogin"),
     path('visitorLogin/', views.visitorLogin, name = "visitorLogin"),
     path('visitorSignUp/doVisitorSignUp/',views.doVisitorSignUp,name="doVisitorSignUp"),
     path('residentSignUp/doResidentSignUp/',views.doResidentSignUp,name="doResidentSignUp"),

]