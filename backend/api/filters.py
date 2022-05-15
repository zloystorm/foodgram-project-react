from django_filters import AllValuesMultipleFilter
from django_filters import rest_framework as filters
from django_filters.widgets import BooleanWidget
from recipes.models import Recipe


class TagFavoritShopingFilter(filters.FilterSet):
    is_in_shopping_cart = filters.BooleanFilter(widget=BooleanWidget())
    is_favorited = filters.BooleanFilter(widget=BooleanWidget())
    tags = AllValuesMultipleFilter(field_name="tags__slug")
    author = AllValuesMultipleFilter(field_name="author__id")

    class Meta:
        model = Recipe
        fields = ["author__id", "tags__slug",
                  "is_favorited", "is_in_shopping_cart"]


class IngredientSearchFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='startswith')

    class Meta:
        model = Ingredient
        fields = ('name', )
