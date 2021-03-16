from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Issue(models.Model):

    def __str__(self):
        return self.issue_place
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    issue_place = models.CharField(max_length=200)
    issue_desc = models.CharField(max_length=200)
    issue_period = models.IntegerField()
    issue_image = models.CharField(max_length=500,default="https://www.economist.com/img/b/1280/720/90/sites/default/files/images/2019/06/articles/main/20190622_std001.jpg")

    def get_absolute_url(self):
        return reverse("waste:detail", kwargs={"pk": self.pk})