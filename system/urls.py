from django.urls import path

from system.views import *


urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
]
