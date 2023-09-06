from django.urls import path

from home.apps import HomeConfig
from home.views import HomePageView, GuestPageView

app_name = HomeConfig.name

urlpatterns = [
    path('', GuestPageView.as_view(), name='quest'),
    path('home', HomePageView.as_view(), name='index'),
]
