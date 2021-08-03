from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):
    print(request.GET)
    return HttpResponse("Hello World")


def home(request):
    print(request.POST.get("username"))
    return render(request,
                  'index.html',
                  context={"username": request.POST.get("username", "world")})


def get_max_string(request):
    longest = str(request.POST.get("string1"))
    if len(str(request.POST.get("string2"))) > len(longest):
        longest = str(request.POST.get("string2"))
    if len(str(request.POST.get("string3"))) > len(longest):
        longest = str(request.POST.get("string3"))
    return render(request,
                  'max_string.html',
                  context={"longest": longest})


def get_date(request):
    date_str = request.POST.get("date", "none")
    if date_str != "none":
        print(date_str)
        date = datetime.strptime(date_str, "%Y-%m-%d")
        day = date.day
        month = date.month

        if day == 1 and month == 1:
            year = date.year
            date_str = f'Happy {year} New Year!'

        return render(request,
                      'date.html',
                      context={"date": date_str})
    else:
        return render(request,
                      'date.html')
