import base64
import json
from django.db import models
from cryptography.fernet import Fernet
import os
from django.utils.timezone import now,localtime
# from django.utils import timezone
from dotenv import load_dotenv
import pytz

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
cipher = Fernet(SECRET_KEY.encode())

class AuthSession(models.Model):
    key_ss = models.CharField(primary_key=True,max_length=255)
    token_ss = models.TextField()
    expireDate_ss = models.DateTimeField()

    def save_sesssion_data(self, data):
        """
        เข้ารหัสและบันทึก session_data
        :param data: Dictionary ที่ต้องการเก็บใน session
        """
        serialized_data = json.dumps(data) # แปลงเป็น json
        encrypted_data = cipher.encrypt(serialized_data.encode()) # เข้ารหัส
        self.token_ss = base64.urlsafe_b64encode(encrypted_data).decode() # แปลงเป็น base 64 string for save to DB

    def get_session_data(self):
        """
        ถอดรหัสและดึงข้อมูล session_data
        :return: Dictionary ของ session data
        """
        try:
            encrypted_data = base64.urlsafe_b64decode(self.token_ss.encode())
            decrypted_data = cipher.decrypt(encrypted_data).decode()
            return json.loads(decrypted_data)
        except Exception:
            return {}
    
    def delete_session_data(self):
        self.delete()
        
    def is_expired(self):
        """
        ตรวจสอบว่า session หมดอายุหรือไม่
        :return: True ถ้า session หมดอายุ
        """
        
        # return now().astimezone(pytz.timezone('Asia/Bangkok')) > self.expireDate_ss.astimezone(pytz.timezone('Asia/Bangkok'))
        # return now() > self.expireDate_ss
        print(f"""{now()} -> {self.expireDate_ss} : {now() > self.expireDate_ss}""")
        return now() > self.expireDate_ss
    
    def __str__(self):
        return self.key_ss
    
    class Meta:
        managed = False
        db_table = 'auth_session'