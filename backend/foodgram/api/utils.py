from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from recipes.models import Favorite, ShoppingCart
from users.models import Subscription


def get_cart_txt(ingredients):
    """Function to generate txt file for shopping list."""
    content_list = []
    for ingredient in ingredients:
        content_list.append(
            f'{ingredient["ingredient__name"]} '
            f'({ingredient["ingredient__measurement_unit"]}): '
            f'{ingredient["total_amount"]}')
    content = 'Ваш список покупок:\n\n' + '\n'.join(content_list)
    filename = 'shopping_cart.txt'
    file = HttpResponse(content, content_type='text/plain')
    file['Content-Disposition'] = 'attachment; filename={0}'.format(
        filename)
    return file


MODELS = {
    Subscription: {
        'name': 'author',
        'err_exist': 'Вы уже подписаны на этого пользователя!',
        'err_not_exist': 'Вы не подписаны на этого пользователя!',
    },
    Favorite: {
        'name': 'recipe',
        'err_exist': 'Этот рецепт уже в избранном!',
        'err_not_exist': 'Этого рецепта нет в избранном!',
    },
    ShoppingCart: {
        'name': 'recipe',
        'err_exist': 'Этот рецепт уже в корзине!',
        'err_not_exist': 'Этого рецепта нет в корзине!',
    },
}


def post_for_actions(user, obj, model):
    """Function for post request actions."""
    args = {MODELS[model]['name']: obj,
            'user': user}
    post_obj = model(**args)
    if model.objects.filter(**args).exists():
        raise serializers.ValidationError(MODELS[model]['err_exist'])
    post_obj.save()


def delete_for_actions(user, obj, model):
    """Function for delete request actions."""
    args = {MODELS[model]['name']: obj,
            'user': user}
    if not model.objects.filter(**args).exists():
        raise serializers.ValidationError(MODELS[model]['err_not_exist'])
    del_obj = get_object_or_404(model, **args)
    del_obj.delete()
