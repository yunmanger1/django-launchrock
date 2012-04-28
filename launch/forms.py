#coding: utf-8
from mongotools.forms import MongoForm
from django import forms
from launch.entities import LaunchRock


class LaunchRockForm(MongoForm):
    class Meta:
        document = LaunchRock
        exclude = ('sign_date', 'ip', 'http_refer')

    def clean_email(self):
        try:
            LaunchRock.objects.get(email=self.cleaned_data['email'])
        except LaunchRock.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(u"Спасибо вам, но этот email уже имеется в базе.")


class LaunchRockAdminForm(MongoForm):
    class Meta:
        document = LaunchRock

    def clean_email(self):
        try:
            LaunchRock.objects.get(email=self.cleaned_data['email'])
        except LaunchRock.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(u"Этот email уже имеется в базе.")
