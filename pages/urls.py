from django.urls import path
from .views import homt_page_view

urlpatterns = [
    path("",homt_page_view,name='home')
]