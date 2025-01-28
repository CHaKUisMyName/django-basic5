from django.db import models
from django.core.exceptions import ObjectDoesNotExist

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

    # การใช้ @classmethod ทำให้คุณสามารถเรียก method ได้จากตัว class โดยไม่จำเป็นต้องสร้าง instance ของ class ก่อน
    @classmethod
    def getUserById(self, userid):
        """
        ดึงข้อมูล User จาก id_u
        """
        try:
            return self.objects.get(id_u=userid)
        except ObjectDoesNotExist:
            return None 

    class Meta:
        managed = False
        db_table = 'user'