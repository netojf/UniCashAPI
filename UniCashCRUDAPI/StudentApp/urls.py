from django.urls import re_path
from StudentApp import views

urlpatterns = [
    re_path(r'^student$',views.StudentAPI),
    re_path(r'^student/([0-9]+)$',views.StudentAPI),
]



