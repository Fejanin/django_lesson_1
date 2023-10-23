from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return HttpResponse('Страницо о роботах')

def categories(request, catid):
    name = "EMPTY"
    if request.GET:
        print(str(request.GET), type(str(request.GET)))
        name = request.GET["name"]
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p><p>{name}</p>')

def archive(request, year):
    if int(year) > 2020:
        raise Http404
    elif int(year) < 2000:
        # permanent=True - если страница/сайт перемещены на новый адрес навсегда
        return redirect('home', permanent=True) # перенаправление, в данном случае на главную страницу
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')