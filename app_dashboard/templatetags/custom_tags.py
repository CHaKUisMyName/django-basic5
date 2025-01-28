from django import template
from django.http import HttpRequest
from app_users.models.authsession import AuthSession
from app_users.models.user import User

register = template.Library()

@register.simple_tag(takes_context=True)
def get_user(context):
    request: HttpRequest = context['request']
    token = request.COOKIES.get("session")
    session = AuthSession.objects.get(key_ss=token)
    data = session.get_session_data()
    user = User.objects.get(id_u=data['user_id'])
    if user:
        return user.email_u
    return None