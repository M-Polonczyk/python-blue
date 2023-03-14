from django.conf import settings
import random
import string



SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, length=SHORTCODE_MIN):
    new_code = code_generator(size=length)
    Klass = instance.__class__   
    # print(Klass)
    qs = Klass.objects.filter(shortcode=new_code).exists()
    if qs:
        return create_shortcode(length=length)
    return new_code
