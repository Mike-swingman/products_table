from django.urls import path
from views import PublishedFoodListView

urlpatterns = [
    path('api/food-list/', PublishedFoodListView.as_view(), name='published_food_list'),
]
