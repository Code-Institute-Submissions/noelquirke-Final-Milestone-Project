from django.contrib import admin
from django.urls import path

from .views import CreateEmailView

urlpatterns = [
    path('', CreateEmailView.as_view(), name='email-form'),
]
