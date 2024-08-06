from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Prefetch, Count, Q

from models import FoodCategory, Food
from serializers import FoodListSerializer


class PublishedFoodListView(APIView):

    def get(self, request):
        """ Функция отдает категории блюд, в которых содержится хотя бы одно опубликованное блюдо """

        categories_with_published_foods = (
            FoodCategory.objects.annotate(
                published_foods_count=Count('food', filter=Q(food__is_publish=True))
                ).filter(published_foods_count__gt=0).prefetch_related(
                Prefetch('food', queryset=Food.objects.filter(is_publish=True))
                )
        )

        serializer = FoodListSerializer(categories_with_published_foods, many=True)

        return Response(serializer.data)
