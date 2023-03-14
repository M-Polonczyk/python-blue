from django import forms
from .validators import validate_url, validate_com

'''
DO NAPRAWY
'''

class SubmitURLform(forms.Form):
    url = forms.CharField(
        label='Submit URL',
        validators=[validate_url],
        widget= forms.TextInput(
        attrs={
                'placeholder':  'Submit your URL',
                'class':        'form-control'
              }
        )
        )
    
    # def clean(self) -> Dict[str, Any]:
    #     cleaned_data = super().clean()
    #     url = cleaned_data.get('url')
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError('Invalid URL')
    #     return {'url': url}

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except ValidationError:
    #         raise forms.ValidationError('Invalid URL')
    #     return url
 