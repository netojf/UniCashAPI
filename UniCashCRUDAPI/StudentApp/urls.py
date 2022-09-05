from django.conf.urls import url
from StudentApp import views

urlpatterns = [
    url(r'^student$',views.StudentAPI),
    url(r'^student/([0-9]+)$',views.StudentAPI),
]



