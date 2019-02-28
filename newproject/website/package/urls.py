from django.conf.urls import url
#from django.urls import path
from package import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(' ', views.my_view1,name='my_view_name1'),
    url(' ', views.my_view2,name='my_view_name2'),

]
