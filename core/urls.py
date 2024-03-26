import os
from django.contrib import admin
from django.urls import path
from.wiew import first_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first_page),
]
