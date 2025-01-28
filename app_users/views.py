import json
import os
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from cryptography.fernet import Fernet
import secrets
from datetime import timedelta
from django.urls import reverse
from django.utils.timezone import now,localtime
import pytz
from app_users.models.authsession import AuthSession
from app_users.models.authuser import AuthUser, verify_password
from app_users.models.level import Level
from app_users.models.user import User
from dotenv import load_dotenv
from django.contrib import messages

from app_users.utils import custom_is_login

load_dotenv()

@custom_is_login
def index(request: HttpRequest):
    levels = Level.objects.all()
    # print(os.getenv('SECRET_KEY'))

    users = User.objects.all()
    authUsers = AuthUser.objects.all()
    userList = []
    for user in users:
        userList.append(
            {
                'id_u':user.id_u,
                'fullName': user.fName_u+" "+user.lName_u,
                'hasAccount': any(authUser.id_u_auth == user.id_u for authUser in authUsers)
            }
        )

    context = {
        "levels":levels,
        "userList": userList,
    }
    return render(request,'user/index.html',context)

def login(request: HttpRequest):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"""email : {email} -> pass : {password}""")

        authUser = AuthUser.objects.filter(email_auth = email).first()
        # print(authUser.__dict__)
        if authUser == None:
            messages.error(request, 'Not Found User')
            return HttpResponseRedirect('/login')
        print(f"""verify_password(password, authUser.pass_auth)  : {verify_password(password, authUser.pass_auth)}""")
        if not verify_password(password, authUser.pass_auth):
            messages.error(request, 'wrong password')
            return HttpResponseRedirect('/login')
        
        # create auth session
        session = AuthSession()
        session.key_ss = secrets.token_hex(20)
        session.expireDate_ss = now()+timedelta(days=1)
        session.save_sesssion_data({'user_id': authUser.id_u_auth})
        session.save()

        # update time stamp login
        authUser.lastLogin_auth = now()
        authUser.save()

        response = HttpResponseRedirect('/')
        response.set_cookie('session',session.key_ss,expires=session.expireDate_ss)
        return response
    else:
        return render(request, 'user/login.html')
    
def logout(request: HttpRequest):
    token = request.COOKIES.get("session")
    authSession = AuthSession.objects.get(key_ss=token)
    authSession.delete()
    response = HttpResponseRedirect('/login')
    response.delete_cookie('session')
    return response

@custom_is_login    
def addUser(request: HttpRequest):
    if request.method == "POST":
        user = User()
        user.title_u = request.POST.get('title')
        user.fName_u = request.POST.get('fname')
        user.mName_u = request.POST.get('mname')
        user.lName_u = request.POST.get('lname')
        user.email_u = request.POST.get('email')
        user.isAdmin_u = 1 if request.POST.get('isadmin') is not None else 0
        user.isActive_u = 1
        user.save()
        print(user.__dict__)

        response = HttpResponseRedirect(reverse('userIndex'))
        return response
        # print(request.POST.get('isadmin')) # จะคืนค่า "on" ถ้าติ๊ก, หรือ None ถ้าไม่ได้ติ๊ก
    else:
        pass
    return render(request, 'user/adduser.html')

@custom_is_login
def regis(request: HttpRequest, id_u):
    print(id_u)
    user = User.objects.get(id_u = id_u)
    if request.method == "POST":
        authUser = AuthUser()
        authUser.email_auth = request.POST.get('email')
        authUser.hash_password(request.POST.get('password'))
        authUser.isActive_auth = 1
        authUser.id_u_auth = id_u
        authUser.cDate_auth = now()
        authUser.save()
        # ใช้ reverse เพื่อดึง URL จาก name ของ urls เป็น string
        response = HttpResponseRedirect(reverse("userIndex"))
        return response
    else:
        context = {
            "user":user
        }
        return render(request, 'user/regis.html',context)