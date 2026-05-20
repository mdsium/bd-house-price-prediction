from django.urls import path
from .views import PredictPriceAPIView, ContactFormAPIView, PredictionHistoryAPIView

urlpatterns = [
    path('predict/', PredictPriceAPIView.as_view(), name='predict-price'),
    path('contact/', ContactFormAPIView.as_view(), name='contact-form'),
    path('predictions/history/', PredictionHistoryAPIView.as_view(), name='prediction-history'),
]