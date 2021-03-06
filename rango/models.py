from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=128,unique=True)
    views = models.IntegerField(default=0)
    likes=models.IntegerField(default=0)
    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images',blank=True)
    address = models.TextField(blank=True)
    company = models.TextField(blank=True)


    def __unicode__(self):
        return self.user.username


class CategoryComment(models.Model):
    comment=models.CharField(max_length=120)
    category=models.ForeignKey(Category,null=True)
    title=models.CharField(max_length=100,default="null")

    def __unicode__(self):
        return self.comment



