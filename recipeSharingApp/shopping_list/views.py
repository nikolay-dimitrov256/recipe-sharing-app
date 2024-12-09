import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView

from recipeSharingApp.recipes.models import Recipe
from recipeSharingApp.shopping_list.models import ShoppingList


class ShoppingListDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ShoppingList
    template_name = 'shopping_list/shopping-list-details.html'

    def test_func(self):
        shopping_list = get_object_or_404(ShoppingList, pk=self.kwargs['pk'])

        return self.request.user == shopping_list.user


@login_required
def send_recipe_ingredients_to_shopping_list(request, pk, recipe_id):
    shopping_list = get_object_or_404(ShoppingList, pk=pk)

    if shopping_list.user != request.user:
        return HttpResponseForbidden

    recipe = Recipe.objects.get(pk=recipe_id)

    for product, quantity in recipe.ingredients.items():
        shopping_list.products[product] = quantity

    shopping_list.save()

    return redirect('shopping-list-details', pk=pk)


@login_required
def edit_shopping_list_view(request, pk):
    shopping_list = get_object_or_404(ShoppingList, pk=pk)

    if shopping_list.user != request.user:
        return HttpResponseForbidden

    if request.method == 'POST':
        products_json = request.POST.get('ingredients_json')

        try:
            products = json.loads(products_json)
        except json.JSONDecodeError:
            return HttpResponseBadRequest

        shopping_list.products = products
        shopping_list.save()
        return redirect('shopping-list-details', pk)

    context = {
        'shopping_list': shopping_list
    }

    return render(request, 'shopping_list/edit-shopping-list.html', context)


@login_required
def clear_shopping_list_view(request, pk):
    shopping_list = get_object_or_404(ShoppingList, pk=pk)

    if shopping_list.user != request.user:
        return HttpResponseForbidden

    if request.method == 'POST':
        shopping_list.products = {}
        shopping_list.save()

        return redirect('shopping-list-details', pk)

    context = {
        'shopping_list': shopping_list,
    }

    return render(request, 'shopping_list/clear-shopping-list.html', context)
