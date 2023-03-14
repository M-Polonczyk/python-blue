from django.db import models
from shortener.models import KirrURL
import datetime

# Create your models here.

class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, KirrURL):
            obj, created = self.get_or_create(kirr_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    kirr_url    = models.ForeignKey(KirrURL, on_delete=models.CASCADE)
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(default=datetime.datetime.now)

    objects = ClickEventManager()

    def __str__(self) -> str:
        return '{i}'.format(i=self.count)