from django.shortcuts import render
from django.http import HttpResponse
import django.contrib.staticfiles
import os
# Create your views here.
# def home(request):
#     posts = [
#         {
#             'value':0
#         },
#         {
#             'value':1
#         },
#         {
#             'value':2
#         }
#     ]
#     context = {'posts':posts}
#     return render(request, 'blog/home.html', context)
def home(request):
    # result = request.GET.get('your_name')
    # print("Result: ",result)
    # s=""
    # print(os.getcwd())
    # with(open('./blog/files/t.txt','r')) as f:
    #    s = f.read()
    return render(request, 'blog/index.html',{'result': s})
def kadoi(request):
    
    return render(request, 'blog/kadoi.html')

def anakiklosima(request):
    # result = request.GET.get('your_name')
    # print("Result: ",result)
    # s=""
    # print(os.getcwd())
    # with(open('./blog/files/t.txt','r')) as f:
    #    s = f.read()
    return render(request, 'blog/anakiklosima.html')

def antamoivi(request):
    return render(request, 'blog/antamoivi.html')

def about(request):
    return render(request, 'blog/about.html')