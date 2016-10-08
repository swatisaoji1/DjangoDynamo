from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^new/$', views.new_student, name='new_student'),
    url(r'^edit/(.*)$', views.edit_student, name='edit_student'),
    url(r'^delete/(.*)$', views.delete_student, name='delete_student'),
]