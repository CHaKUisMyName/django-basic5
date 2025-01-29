from django.http import HttpRequest

from app_users.models.authsession import AuthSession
from app_users.models.user import User


class UserInjectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        token = request.COOKIES.get("session")
        # session = AuthSession.objects.get(key_ss=token)
        session = AuthSession.objects.filter(key_ss=token).first()
        if session is not None:
            if not session.is_expired():
                data = session.get_session_data()
                user = User.getUserById(data['user_id'])
                request.current_user = user
            else:
                request.current_user = None
        else:
            request.current_user = None
        
        response = self.get_response(request)
        return response