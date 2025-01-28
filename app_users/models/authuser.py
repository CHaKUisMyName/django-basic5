import logging
from django.db import models
from passlib.context import CryptContext

# https://github.com/pyca/bcrypt/issues/684
#AttributeError: module 'bcrypt' has no attribute '__about__' with new 4.1.1 version #684
logging.getLogger('passlib').setLevel(logging.ERROR)

# สร้าง CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(password: str, hashPassword: str):
    return pwd_context.verify(password, hashPassword)

class AuthUser(models.Model):
    id_auth = models.AutoField(primary_key=True)
    email_auth = models.CharField(max_length=255,null=False,blank=False)
    pass_auth = models.CharField(max_length=255,blank=False,null=False)
    lastLogin_auth = models.DateTimeField(null=True)
    isActive_auth = models.SmallIntegerField()
    id_u_auth = models.IntegerField()
    cDate_auth = models.DateTimeField(null=True)

    def hash_password(self, password: str):
        self.pass_auth = pwd_context.hash(password)

    class Meta:
        managed = False
        db_table = 'auth_user'