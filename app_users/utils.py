from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from app_users.models.authsession import AuthSession


def custom_is_login(view_func):
    def wrapper(request: HttpRequest, *args,**kwargs):
        try:
            token = request.COOKIES.get("session")
            # session = AuthSession.objects.get(key_ss=token)
            session = AuthSession.objects.filter(key_ss=token).first()
            # print(session.is_expired())
            if session is not None:
                if not session.is_expired():
                    data = session.get_session_data()
                    # print(data)
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