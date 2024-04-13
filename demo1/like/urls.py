from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for liking an item
    path('like/<int:item_id>/', views.like_item, name='like_item'),

    # URL pattern for unliking an item
    path('unlike/<int:item_id>/', views.unlike_item, name='unlike_item'),
]