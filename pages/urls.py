from django.urls import path
from pages.views import HomePageView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
]