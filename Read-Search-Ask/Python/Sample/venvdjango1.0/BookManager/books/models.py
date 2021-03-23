from django.db import models

# Create your models here.

class BookInfo(models.Model):
    # 主键当前可以自动生成
    # 书名
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class PersonInfo(models.Model):
    # 人名
    name = models.CharField(max_length=10)
    # 性别
    gender = models.BooleanField()
    # 外键
    book = models.ForeignKey(BookInfo)
