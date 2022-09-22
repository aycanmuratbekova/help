from django.contrib import admin
from django.urls import path, include
from .views import CategoryAPIView, DonationViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('categories/', CategoryAPIView.as_view()),
    path('donation/', DonationViewSet.as_view({'get': 'list'})),
    # path('')
]
