from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from typing import Dict, Any
'''
DO NAPRAWY
'''

def validate_url(value):
    # url_validator = URLValidator()
    # if not 'http://' or 'https://' in value:
    #     value = 'http://' + value
    # try:
    #     url_validator(value)
    # except:
    #     raise ValidationError('Invalid URL')
    return value


def validate_com(value):
    # if not 'com' in value:
    #     raise ValidationError('Not .com in URL')
    return value





'''
   def clean_url(self):
        url_validator = URLValidator()
        url = self.cleaned_data['url']
        try:
            url_validator(url)
        except:
            raise forms.ValidationError('Invalid URL')
        return url
    def clean(self):
        cleaned_data = super(SubmitURLform, self).clean()
        url = cleaned_data
class ContactForm(forms.Form):
    # Everything as before.
    ...

    def clean(self):
        cleaned_data = super().clean()
        cc_myself = cleaned_data.get("cc_myself")
        subject = cleaned_data.get("subject")

        if cc_myself and subject:
            # Only do something if both fields are valid so far.
            if "help" not in subject:
                raise ValidationError(
                    "Did not send for 'help' in the subject despite "
                    "CC'ing yourself."
                )
'''