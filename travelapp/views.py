from django.shortcuts import render
from django.http import HttpResponse 
from . models import place
from . models import blog
# Create your views here.
def fun(request):
    obj=place.objects.all()


    # return render(request,'index.html',{'results':obj})
    obj1 = blog.objects.all()
    return render(request, 'index.html', {'cont': obj1,'results':obj})
# def blog(request):
#     obj = blog.objects.all()
#     return render(request,'index.html',{'cont':obj})


def addition(request):
    num1=int(request.POST["num1"])
    num2=int(request.POST["num2"])
    num3=num1+num2
    return render(request,'result.html',{'add':num3})