from django import forms
from django.forms import widgets
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UsernameField, AuthenticationForm


class SignUpForm(forms.ModelForm):
    username = UsernameField(
        label=('Username'),
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control',
                                      'placeholder': 'Your username for login'}),
    )

    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True, 'class': 'form-control',
                                          'placeholder': 'Your password for login'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta:
        model = get_user_model()
        fields = ('username',  'password',)

    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_active = True
        user.save()
        return user


class SignInForm(forms.ModelForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control',
                                      'placeholder': 'Your username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Your password'}),
    )

    class Meta:
        model = get_user_model()
        fields = ('username',  'password',)

