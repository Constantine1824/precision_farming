from django.urls import path
from .views import PrecisionAPIView, HealthStatusAPIView

urlpatterns = [
    path('', HealthStatusAPIView.as_view(), name='status'),
    path('result', PrecisionAPIView.as_view(), name='precision')
]
