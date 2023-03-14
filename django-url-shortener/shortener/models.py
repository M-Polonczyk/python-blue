from django.conf import settings
from django.db import models
from django.urls import reverse
from .utils import create_shortcode
from .validators import validate_url, validate_com
import datetime

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)

class KirrURL_Manager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(KirrURL_Manager, self).all(*args, **kwargs).filter(active=True)
        return qs

    def refresh_shortcodes(self, items=100):
        new_codes = 0
        qs = KirrURL.objects.filter(id__gte=1)
        if items != 100 and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return 'New codes made: {i}'.format(i=new_codes)

class KirrURL(models.Model):
    url         = models.CharField(max_length=220, validators=[validate_url])
    shortcode   = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(default=datetime.datetime.now)
    active      = models.BooleanField(default=True)
    objects     = KirrURL_Manager()

    def __str__(self) -> str:
        return str(self.url)
    
    def __unicode__(self):
        return str(self.url)

    def save(self, *args, **kwargs) -> None:
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        return super(KirrURL, self).save(*args, **kwargs)
    
    def get_url(self):
        # url_path = reverse('shortcode', kwargs={'shortcode': self.shortcode})
        # return 'http://myshortener.com:8000/' + url_path
        return 'http://myshortener.com:8000/{shortcode}'.format(shortcode=self.shortcode)
        