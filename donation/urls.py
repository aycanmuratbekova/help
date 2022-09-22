from django.contrib import admin
from django.urls import path, include
from .views import CategoryAPIView, DonationAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('categories/', CategoryAPIView.as_view()),
    path('donation/<int:category_id>', DonationAPIView.as_view()),
    # path('')
]
