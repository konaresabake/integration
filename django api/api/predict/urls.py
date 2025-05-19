from django.urls import path
from .views import predict_budget, home

urlpatterns = [
    path('', home),
    path('predict/', predict_budget),
]
