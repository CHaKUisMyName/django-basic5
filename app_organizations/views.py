from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.timezone import now
from django.contrib import messages

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
        try:
            curUser: User = request.current_user
            org = Organization()
            org.code_org = request.POST.get('code')
            org.nameTH_org = request.POST.get('nameth')
            org.nameEN_org = request.POST.get('nameen')
            # org.isActive_org = 1 if request.POST.get('isactive') is not None else 0
            org.isActive_org = 1
            org.cDate_org = now()
            org.uDate_org = now()
            org.cId_u_org = curUser.id_u
            org.uId_u_org = curUser.id_u
            org.save()

            messages.success(request,'Save Success')
            
            # user.isAdmin_u = 1 if request.POST.get('isadmin') is not None else 0

            # response = HttpResponseRedirect(reverse('indexOrg'))
        except Exception:
            messages.error(request, 'Error!!!')
            # response = HttpResponseRedirect(reverse('addOrg'))
        response = HttpResponseRedirect(reverse('indexOrg'))
        return response
    else:
        user: User = request.current_user
        
        print(user.fName_u)
    return render(request,'organization/addorg.html')

@custom_is_login
def editOrganization(request: HttpRequest, orgid):
    org = Organization.objects.filter(id_org = orgid).first()
    if org is None:
        messages.error(request,'Not Found Data')
        return HttpResponseRedirect(reverse('indexOrg'))
    context = {
        'org': org,
    }
    return render(request,'organization/editorg.html',context)