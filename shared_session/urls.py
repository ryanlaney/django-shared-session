from django.conf.urls import re_path
from . import views

app_name = "shared_session"

urlpatterns = [
    re_path(r'^(?P<message>.+).js$', views.shared_session_view, name='share'),
]