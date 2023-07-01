from django.urls import path
from .views import ProductsList, ProductDetail, multiply

urlpatterns = [
   path('', ProductsList.as_view()),
   path('<pk>', ProductDetail.as_view()),
   path('multiply/', multiply),
]
