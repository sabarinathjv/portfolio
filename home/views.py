from django.shortcuts import render,HttpResponse#htttp
from home.models import Contact #for data base

def home(request):#fn created
    #return HttpResponse('this is my home page')
    context = {'name':'sabari','course':'django'}#repeat ayi varunna sadam dict akki eve edum(html il varanann e chyynnath)
    return render(request,'home.html',context)# context vach athine home nu akath varuthum


def about(request):#fn created
    return render(request,'about.html')


def projects(request):#fn created
    return render(request,'projects.html')


def contact(request):#fn created
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
       # print(name,email,phone,desc)
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        print('the data is saved')
        
    return render(request,'contact.html')







