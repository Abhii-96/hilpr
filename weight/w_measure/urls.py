from django.conf.urls import url
from w_measure import views

urlpatterns = [
     url(r'^$',views.index,name='index'),
     
]
