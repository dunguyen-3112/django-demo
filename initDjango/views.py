from django.http import JsonResponse
from .models import Drink
from .serilazers import DrinkSericlizer


def drink_list(request):
    drinks = Drink.objects.all()
