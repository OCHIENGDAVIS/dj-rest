from django.urls import path, include

from .views import APIHome


app_name = 'api'
urlpatterns = [
    path('', APIHome.as_view(), name='home'),
    path('products/', include('products.urls', namespace='products'))
]
