from django.urls import path

from app_organizations import views


urlpatterns = [
    path('',views.index, name='indexOrg'),
    path('addorg/', views.addOrganization, name='addOrg')
]