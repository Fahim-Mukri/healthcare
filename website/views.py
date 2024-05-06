from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello world")


def dashboard(request):
    
    context = {"msg":[1,2,3,4,5,6,7,8,9],"names":["Sachin","Fahim","Gaurang","Ankita"]}

    return render(request, "dashboard.html",context) 

def home(request):
    msg = "hello world from views"
    secondmsg = "hello hello"
    data = {"msg":msg,"secondmsg":secondmsg}
    return render(request, "home.html",data)