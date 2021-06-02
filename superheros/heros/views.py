from django.shortcuts import render
from .models import Hero 
# Create your views here.


def index(request):
    all_heros = Hero.objects.all()

    context = {
        'all_heros' : all_heros
    }

    return render(request, 'heros/index.html', context)
