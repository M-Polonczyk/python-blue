from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from shortener.validators import validate_url
from .models import KirrURL
from .forms import SubmitURLform
from analytics.models import ClickEvent
# Create your views here.

# def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
#     obj = get_object_or_404(KirrURL, shortcode=shortcode)
#     return HttpResponse('Hello {sc}'.format(sc=obj.url))

class HomeView(View):
    form = SubmitURLform()
    context = {
            'title':'Submit URL',
            'form':form}
    def get(self, request, *args, **kwargs):
        return render(request, 'shortener/home.html', {})
    
    def post(self, request, *args, **kwargs):   
        self.form = SubmitURLform(request.POST) 
        template = 'shortener/home.html'
        if self.form.is_valid():
            # new_url = self.form.cleaned_data.get('url')
            obj, created = KirrURL.objects.get_or_create(url=self.form.cleaned_data.get('url'))
            self.context = {
                'object':obj,
                'created':created
                }  
            if created:
                template = 'shortener/success.html'
            else:
                template = 'shortener/already-exists.html'
        # return KirrRedirectView.get(self, request)
        return render(request, template, self.context)



class KirrRedirectView(View):

    def get(self, request, shortcode=None,*args, **kwargs):
        print(shortcode)
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)

    def post(self, request, *args, **kwargs):
        return HttpResponse()
    





'''
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
    obj_url = None
    qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    if qs.exists() and qs.count() == 1:
        obj = qs.first()
        obj_url = obj.url
    return HttpResponse('Hello {sc}'.format(sc=obj_url))
'''