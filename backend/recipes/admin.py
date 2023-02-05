from django.contrib.admin import ModelAdmin, StackedInline, display, register

from .models import (FavoriteRecipe, Ingredient, Recipe, RecipeIngredient,
                     ShoppingCart, Subscribe, Tag)

EMPTY_MSG = '-пусто-'


class RecipeIngredientAdmin(StackedInline):
    model = RecipeIngredient
    autocomplete_fields = ('ingredient',)


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = (
        'id', 'get_author', 'name', 'text',
        'cooking_time', 'get_tags', 'get_ingredients',
        'pub_date', 'get_favorite_count')
    search_fields = (
        'name', 'cooking_time',
        'author__email', 'ingredients__name')
    list_filter = ('pub_date', 'tags',)
    inlines = (RecipeIngredientAdmin,)
    empty_value_display = EMPTY_MSG

    @display(
        description='Электронная почта автора')
    def get_author(self, obj):
        return obj.author.email

    @display(description='Тэги')
    def get_tags(self, obj):
        list_ = [_.name for _ in obj.tags.all()]
        return ', '.join(list_)

    @display(description=' Ингредиенты ')
    def get_ingredients(self, obj):
        return '\n '.join([
            f'{item["ingredient__name"]} - {item["amount"]}'
            f' {item["ingredient__measurement_unit"]}.'
            for item in obj.recipe.values(
                'ingredient__name',
                'amount', 'ingredient__measurement_unit')])

    @display(description='В избранном')
    def get_favorite_count(self, obj):
        return obj.favorite_recipe.count()


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = (
        'id', 'name', 'color', 'slug',)
    search_fields = ('name', 'slug',)
    empty_value_display = EMPTY_MSG


@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = (
        'id', 'name', 'measurement_unit',)
    search_fields = (
        'name', 'measurement_unit',)
    empty_value_display = EMPTY_MSG


@register(Subscribe)
class SubscribeAdmin(ModelAdmin):
    list_display = (
        'id', 'user', 'author', 'created',)
    search_fields = (
        'user__email', 'author__email',)
    empty_value_display = EMPTY_MSG


@register(FavoriteRecipe)
class FavoriteRecipeAdmin(ModelAdmin):
    list_display = (
        'id', 'user', 'get_recipe', 'get_count')
    empty_value_display = EMPTY_MSG

    @display(
        description='Рецепты')
    def get_recipe(self, obj):
        return [
            f'{item["name"]} ' for item in obj.recipe.values('name')[:5]]

    @display(
        description='В избранных')
    def get_count(self, obj):
        return obj.recipe.count()


@register(ShoppingCart)
class SoppingCartAdmin(ModelAdmin):
    list_display = (
        'id', 'user', 'get_recipe', 'get_count')
    empty_value_display = EMPTY_MSG

    @display(description='Рецепты')
    def get_recipe(self, obj):
        return [
            f'{item["name"]} ' for item in obj.recipe.values('name')[:5]]

    @display(description='В избранных')
    def get_count(self, obj):
        return obj.recipe.count()
