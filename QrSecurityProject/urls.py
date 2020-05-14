from django.contrib import admin
from django.urls import path, include
from user_app import urls as user_urls
from qr_app import urls as qr_urls
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('admin/', admin.site.urls),
    path('user/',include(user_urls)),
    path('qr/', include(qr_urls)),
]
