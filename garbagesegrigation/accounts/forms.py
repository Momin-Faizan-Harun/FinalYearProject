from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User,Generator,Handler
from django import forms


class GeneratorRegisterationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_generator = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        generator = Generator.objects.create(user=user)
        generator.phone_number=self.cleaned_data.get('phone_number')
        generator.save()
        return user


class HandlerRegisterationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_handler = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        handler = Handler.objects.create(user=user)
        handler.phone_number=self.cleaned_data.get('phone_number')
        handler.save()
        return user