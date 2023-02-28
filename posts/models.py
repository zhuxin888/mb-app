from django.db import models


# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(self):  # 展示文字内容
        return self.text[:50]
