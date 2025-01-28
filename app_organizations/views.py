from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app_organizations.models import Organization
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
        print('POST')
        org = Organization()
        org.code_org = request.POST.get('code')
        response = HttpResponseRedirect(reverse('indexOrg'))
        return response
    else:
        pass
    return render(request,'organization/addorg.html')