from django.db import models

# Create your models here.
class DSUser(models.Model):

    name = models.CharField(max_length=128, verbose_name='아이디')
    email = models.EmailField(max_length=128, verbose_name='이메일')
    password = models.CharField(max_length=256, verbose_name='비밀번호')
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='가입일')

    class Meta:
        db_table = 'dstagram_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

    def __str__(self):
        return self.name