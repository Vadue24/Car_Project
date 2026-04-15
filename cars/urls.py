from django.urls import path, include
from rest_framework import routers

from . import views
from .views import ArticleApi

router = routers.DefaultRouter()
router.register(r'api/articles', ArticleApi)

urlpatterns = [
    path('', views.cars_home, name='cars_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.CarsDetailView.as_view(), name='cars_detail'),
    path('<int:pk>/update', views.CarsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', views.CarsDeleteView.as_view(), name='cars_delete'),
    path('', include(router.urls)),
]
