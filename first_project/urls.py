from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'first_project'

urlpatterns = [
  path('hello',views.index, name='index'),
]