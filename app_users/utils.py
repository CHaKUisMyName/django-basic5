from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from app_users.models.authsession import AuthSession
from django.utils.timezone import now
from pprint import pprint

def custom_is_login(view_func):
    def wrapper(request: HttpRequest, *args,**kwargs):
        try:
            token = request.COOKIES.get("session")
            
            # delete session ที่ตกค้าง
            epSeession = AuthSession.objects.filter(expireDate_ss__lt= now())
            if len(epSeession) > 0:
                print('test')
                print(len(epSeession))
                epSeession.delete()

            # หา user
            session = AuthSession.objects.filter(key_ss=token).first()
            if session is not None:
                if not session.is_expired():
                    data = session.get_session_data()
                    print(data)
                else:
                    print("Session expired")
                    session.delete_session_data()
                    response = HttpResponseRedirect('/login')
                    response.delete_cookie('session')
                    return response
            else:
                response = HttpResponseRedirect('/login')
                return response
                # return redirect("/login")
            return view_func(request, *args, **kwargs)
        except AuthSession.DoesNotExist:
            print('session not found')
            return redirect("/login")
    return wrapper