from django.urls import path
from django.conf.urls.static import static
from .views import predict

urlpatterns = [
    path('', predict, name='homepage'),
    ]