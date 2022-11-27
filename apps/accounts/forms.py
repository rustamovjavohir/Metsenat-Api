from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Account


class AccountCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'role', )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(_('Password don\'t match'))
            return password2
        raise forms.ValidationError(_('You should write passwords'))

    def save(self, commit=True):
        account = super().save(commit=False)
        account.set_password(self.cleaned_data['password1'])
        if commit:
            account.save()
        return account


class AccountChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('username', 'email', 'full_name', 'phone', 'image', 'role', 'is_superuser', 'is_staff', 'is_active')

    def __init__(self, *args, **kwargs):
        super(AccountChangeForm, self).__init__(*args, **kwargs)
        self.fields['password'].help_text = '<a href="%s">change password</a>.' % reverse_lazy(
            'admin:auth_user_password_change', args=[self.instance.id])

    def clean_password(self):
        return self.initial['password']