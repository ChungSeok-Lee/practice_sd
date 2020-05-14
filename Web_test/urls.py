from django.urls import path
from Web_test import views
urlpatterns = [
    path("",views.home, name='home'),
]