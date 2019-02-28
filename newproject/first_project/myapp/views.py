# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import textwrap
from django.views.generic.base import View

# Create your views here.
#def foo(request):
#  return HttpResponse("Hello World")
class HomePageView(View):
	def dispatch(request,*args,**kwargs):
		response_text=textwrap.dedent('\
					      <html>\
					      <head>\
					      <title> Input Form </title>\
					      <style>\
					      form {\
					      margin: 0 auto;\
					      width: 400px;\
					      padding: 1em;\
					      border: 1px solid #CCC;\
					      border-radius: 1em;\
					      }\
					      form div + div {\
					      margin-top: 1em;\
					      }\
					      label {\
  					      display: inline-block;\
					      width: 90px;\
					      text-align: right;\
					      }\
					      input, textarea {\
					      font: 1em sans-serif;\
					      width: 300px;\
					      box-sizing: border-box;\
	    				      border: 1px solid #999;\
					      }\
					      input:focus, textarea:focus {\
					      border-color: #000;\
					      }\
					      textarea {\
					      vertical-align: top;\
					      height: 5em;\
					      }\
					      .button {\
					      padding-left: 90px;\
					      }\
					      button {\
					      margin-left: .5em;\
					      }\
					      </style>\
				              </head>\
					      <body>\
					      <form action="/my-handling-form-page" method="post">\
 					      <div>\
   					      <label for="name">Hostname:</label>\
					      <input type="text" id="name" name="host_name">\
					      </div>\
 					      <div>\
					      <label for="mail">Package:</label>\
					      <input type="text" id="pack" name="package_name">\
					      </div>\
	  				      <div>\
					      <div class="button">\
					      <button type="submit">Submit</button>\
					      </div>\
					      </form>\
					      </body>\
					      </html>\
					      ')
		return HttpResponse(response_text)	

