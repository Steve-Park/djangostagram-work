from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그')
    registered_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록일')

    class Meta:
        db_table = 'dstagram_tag'
        verbose_name = '태그'
        verbose_name_plural = '태그'

    def __str__(self):
        return self.naa


class Post(models.Model):
    # 작성자, 이미지 주소, 내용, 작성일, 태그를 저장하는 Post 모델을 만드세요. 작성자는 DSUser 모델과 연결하고 태그는 ag 모델과 다대다 연결을 해주세요

    author = models.ForeignKey(
        'user.DSUser', on_delete=models.CASCADE, verbose_name='작성자')
    imageurl = models.URLField(verbose_name='이미지 URL')
    content = models.TextField(verbose_name='내용')
    tags = models.ManyToManyField('Tag', verbose_name='태그')
    registered_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록일')

    class Meta:
        db_table = 'dstagram_post'
        verbose_name = '게시물'
        verbose_name_plural = '게시물'

    def __str__(self):
        return self.id
