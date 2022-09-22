from django.contrib import admin
from django.urls import path, include
from .views import CategoryAPIView, ArticleAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('categories/', CategoryAPIView.as_view()),
    path('articles/<int:category_id>', ArticleAPIView.as_view()),
    # path('')
]
