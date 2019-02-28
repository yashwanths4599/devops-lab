# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

# Create your views here.
class HomePageView(View):
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)
def my_view1(request):
        if request.method == 'GET':
          import os
          cmd = 'ansible-playbook /root/hostname.yml'
          os.system(cmd)
 
        return HttpResponse('Hostname changed')

def my_view2(request):
        if request.method == 'GET':
          import os
          cmd = 'ansible-playbook /root/install.yml'
          os.system(cmd)

        return HttpResponse('Package Installed')
