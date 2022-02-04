from django.db import models

class User(models.Model):
  user_number = models.BigIntegerField(db_column='User_number', blank=True, null=True)
  user_id = models.TextField(db_column='User_id', blank=True, null=True)
  user_password = models.TextField(db_column='User_password', blank=True, null=True)
  user_name = models.TextField(db_column='User_name', blank=True, null=True)
  user_phonenumber = models.BigIntegerField(db_column='User_phonenumber', blank=True, null=True)
  user_birth = models.DateTimeField(db_column='User_birth', blank=True, null=True)
  user_joindate = models.DateTimeField(db_column='User_joindate', blank=True, null=True)
  user_rate = models.BigIntegerField(db_column='User_rate', blank=True, null=True)

