from django.db import models

class Organization(models.Model):
    id_org = models.AutoField(primary_key=True)
    code_org = models.CharField(max_length=255,blank=True,null=True)
    nameTH_org = models.CharField(max_length=255,blank=True,null=True)
    nameEN_org = models.CharField(max_length=255,blank=True,null=True)
    isActive_org = models.SmallIntegerField(null=True)
    cDate_org = models.DateTimeField(null=True)
    uDate_org = models.DateTimeField(null=True)
    cId_u_org = models.IntegerField(null=True)
    uId_u_org = models.IntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'organization'