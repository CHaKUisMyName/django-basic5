from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.timezone import now

from app_organizations.models import Organization
from app_users.models.user import User
from app_users.utils import custom_is_login

@custom_is_login
def index(request: HttpRequest):
    orgList = Organization.objects.all()
    context = {
        "orgList": orgList,
    }
    return render(request,'organization/index.html', context)

@custom_is_login
def addOrganization(request: HttpRequest):
    if request.method == "POST":
        
        org = Organization()
        org.code_org = request.POST.get('code')
        org.nameTH_org = request.POST.get('nameth')
        org.nameEN_org = request.POST.get('nameen')
        org.isActive_org = 1 if request.POST.get('isactive') is not None else 0
        org.cDate_org = now()
        org.uDate_org = now()
        
        # user.isAdmin_u = 1 if request.POST.get('isadmin') is not None else 0

        response = HttpResponseRedirect(reverse('indexOrg'))
        return response
    else:
        user: User = request.current_user
        print(user.fName_u)
    return render(request,'organization/addorg.html')