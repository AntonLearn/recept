from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

DATA = {
    'Омлет': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'Паста': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'Бутерброд': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}


def home_view(request):
    template_name = 'calculator/home.html'
    keys_list = DATA.keys()
    pages = dict(zip(keys_list, keys_list))
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def recipe_viewer(request, name_dish):
    recipe = DATA.get(name_dish)
    servings = int(request.GET.get('servings', 1))
    if servings <= 0:
        servings = 1
    recipe_servings = dict()
    for ingredient in recipe:
        recipe_servings[ingredient] = round(recipe[ingredient] * servings, 2)
    context = {
        'header': name_dish,
        'servings': servings,
        'recipe_servings': recipe_servings
    }
    template_name = 'calculator/index.html'
    return render(request, template_name, context)