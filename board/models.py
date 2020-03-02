from django.db import models
from django.conf import settings

# Create your models here.
class Board(models.Model):
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name='boards')

    title = models.CharField(max_length=100)
    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subscriber.username + " " + self.title

    # 게시물 목록은 게시물 작성 날짜를 기준으로 최신 날짜로 정렬하세요.
    class Meta:
        ordering = ['-created']