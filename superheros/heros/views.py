from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Hero 

# Create your views here.


def index(request):
    all_heros = Hero.objects.all()

    context = {
        'all_heros' : all_heros
    }

    return render(request, 'heros/index.html', context)

def detail(request, hero_id):
    current_hero = Hero.objects.get(pk=hero_id)
    

    return render(request, 'heros/detail.html', {'current_hero': current_hero})


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter = request.POST.get('alter')
        primary_power = request.POST.get('primary')
        secondary_power = request.POST.get('secondary')
        new_hero = Hero(name=name, alter=alter, primary_power=primary_power, secondary_power=secondary_power)
        new_hero.save()
        return HttpResponseRedirect(reverse('heros:home'))
    else:
        return render(request, 'heros/create.html')



def edit(request, hero_id):
    hero = Hero.objects.get(pk=hero_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        alter = request.POST.get('alter')
        primary_power = request.POST.get('primary')
        secondary_power = request.POST.get('secondary')
        phrase = request.PO.get('phrase')
        current_hero = Hero(id=hero_id, name=name, alter=alter, primary_power=primary_power, secondary_power=secondary_power, catchphrase = phrase)
        current_hero.save()
             
        return HttpResponseRedirect(reverse('heros:home'))
    else:
        return render(request, 'heros/edit.html', {'hero': hero})
   


def delete(request, hero_id): 
    current_hero = Hero.objects.get(pk=hero_id)
    current_hero.delete()
    return HttpResponseRedirect(reverse('heros:home'))