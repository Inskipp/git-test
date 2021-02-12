
from django.urls import path
from .views import start_page

app_name = 'main'

urlpatterns = [
    path('', start_page, name='start_page'),
]
