from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from foods.models import menu

# Create your views here.
def index(request):
    context = dict()
    today = datetime.today().date()
    menus = menu.objects.all() #모든 메뉴 담기
    context["date"] = today
    context["menus"] = menus #menus를 키로 설정
    return render(request, 'foods/index.html', context=context)

def food_detail(request, food):
    context = dict()
    if food == "chicken" :
        context["name"] = "코딩에 빠진 닭"
        context["description"] = "주머니가 가벼운 당신의 가난함을 위한 가격 !"
        context["price"] = 10000
        context["img_path"] = "foods/images/chicken.jpg"
    else :
        raise Http404("그런 음식은 없습니다 !")
    return render(request, 'foods/detail.html', context = context)