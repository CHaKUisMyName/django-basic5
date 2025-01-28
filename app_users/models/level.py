from django.db import models

class Level(models.Model):
    id_lv = models.AutoField(primary_key=True)
    code_lv = models.CharField(max_length=255,blank=True,null=True)
    nameTH_lv = models.CharField(max_length=255,blank=True,null=True)
    nameEN_lv = models.CharField(max_length=255,blank=True,null=True)
    isActive_lv = models.SmallIntegerField(null=True)
    cDate_lv = models.DateTimeField(null=True)
    uDate_lv = models.DateTimeField(null=True)
    cId_u_lv = models.IntegerField(null=True)
    uId_u_lv = models.IntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'level'