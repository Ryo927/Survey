from django.shortcuts import render, HttpResponse, redirect
from surveyapp.models import Data
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'survey.html')
    


def preview(request):   
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        status = request.POST.get('status')
        edu = request.POST.get('edu')
        income = request.POST.get('income')
        gender = request.POST.get('gender')
        context = {'name':name,'email':email,'age':age,'status':status,'edu':edu,'income':income,'gender':gender}
        data=Data(name=name,email=email,age=age,status=status,edu=edu,income=income,gender=gender)
        data.save()
        return render(request,'preview.html',context)
            
    else:
        return HttpResponse('404 - Page not Found')