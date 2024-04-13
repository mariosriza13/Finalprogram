from django.urls import path
from . import views
from .views import items_search

urlpatterns = [
    path('search/', items_search, name='items_search'),
    path('', views.catalog, name='catalog'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),  # URL pattern for category detail view
    path('subcategory/<int:subcategory_id>/', views.subcategory_detail, name='subcategory_detail'),  # URL pattern for subcategory detail vie
]