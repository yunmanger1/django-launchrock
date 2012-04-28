#coding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from launch.entities import LaunchRock
from launch.forms import LaunchRockForm
from django.core.urlresolvers import reverse

import datetime


def _t(name):
    return "launch/%s.html" % name


def signup(request):
    form = LaunchRockForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            LaunchRock.objects.create(email=form.cleaned_data['email'], sign_date=datetime.datetime.now(),
                                    ip=request.META['REMOTE_ADDR'], http_refer=request.META['HTTP_REFERER'])
            return HttpResponseRedirect(reverse('launch-done'))
    return render(request, _t('launch'), {'form': form})


def done(request):
    return render(request, _t('done'))
