from django import forms

from . import css, services

class EmailForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs= {
                'id': 'email-login-input',
                'class': css.EMAIL_FIELD_CSS,
                'placeholder': 'Your email login'
            }
        )
    )
    # class Meta:
    #     model = EmailVerificationEvent
    #     fields = ['email']

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     qs = Email.objects.filter(email=email, active=False)
    #     if qs.exists():
    #         raise forms.ValidationError('Invalid email. Please try again!')
    #     return email

    def clean_email(self):
        email = self.cleaned_data.get('email')
        verified = services.verify_email(email)
        if verified:
            raise forms.ValidationError('Invalid email. Please try again!')
        return email
