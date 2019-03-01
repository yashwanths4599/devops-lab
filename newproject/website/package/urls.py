from django.conf.urls import url
#from django.urls import path
from package import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
   # url('hostname/', views.hostpage.as_view(),name='hostname'),
   # url('install/', views.installpage.as_view(),name='install'),
    url('c_hostname/', views.my_view1,name='my_view_name1'),
    url('p_install/', views.my_view2,name='my_view_name2'),

]
