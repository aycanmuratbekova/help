from django.contrib import admin
from django.urls import path, include
from .views import CategoryAPIView, DonationAPIView, CityListAPIView, DonationDetail, CategoryDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('cities/', CityListAPIView.as_view()),
    path('categories/', CategoryAPIView.as_view()),
    path('categories/<int:pk>', CategoryDetail.as_view()),
    path('donation/', DonationAPIView.as_view()),
    path('donation/<int:pk>', DonationDetail.as_view()),

    # path('donation/<int:cityID>', DonationViewSet.as_view({'get': 'list'}), name='take_by_city'),
    # path('donation/<int:categoryID>/list', DonationViewSet.as_view({'get': 'list'})),
    # path('')
]
