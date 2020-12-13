
from django.contrib import admin
from django.urls import path,include#include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),#give to the app url,include also imported
   
]
