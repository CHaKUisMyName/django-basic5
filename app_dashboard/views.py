from django.http import HttpRequest
from django.shortcuts import render

from app_users.utils import custom_is_login

@custom_is_login
def index(request: HttpRequest):
    
    return render(request, 'dashboard/index.html')