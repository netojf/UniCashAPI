from django.conf.urls import url
from StudentApp import views

urlpatterns = [
    url(r'^student$',views.StudentAPI)
]



