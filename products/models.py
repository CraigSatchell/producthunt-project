from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Product(models.Model):
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=200)
    url = models.CharField(max_length=128)
    pub_date = models.DateTimeField(default=timezone.now)
    votes_total = models.PositiveSmallIntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')

    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title
