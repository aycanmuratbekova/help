from django.contrib import admin
from django.urls import path, include
from .views import Transaction
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('transaction', Transaction)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]

