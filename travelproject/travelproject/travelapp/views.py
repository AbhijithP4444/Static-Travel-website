from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
from .models import People
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=People.objects.all()

    return render(request,"index.html",{'result':obj,'result2':obj2})
# def operations(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add = x + y
#     sub=x-y
#     mult=x*y
#     div=x/y
#
#     return render(request, "result.html", {'add': add,'sub':sub,'mult':mult,'div':div})
#
#
# def about(request):
#
#     return render(request,"about.html")
#
# def contact(request):
#     return render(request,"contact.html")