from django.db import models

class User(models.Model):
    id_u = models.AutoField(primary_key=True)
    code_u = models.CharField(max_length=255,blank=True,null=True)
    title_u = models.CharField(max_length=255,blank=True,null=True)
    fName_u = models.CharField(max_length=255,blank=True,null=True)
    mName_u = models.CharField(max_length=255,blank=True,null=True)
    lName_u = models.CharField(max_length=255,blank=True,null=True)
    email_u = models.CharField(max_length=255,blank=True,null=True)
    isActive_u = models.SmallIntegerField(null=True)
    isAdmin_u = models.SmallIntegerField(null=True)
    id_org_u = models.IntegerField()
    id_lv_u = models.IntegerField()
    cDate_u = models.DateTimeField()
    uDate_u = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'