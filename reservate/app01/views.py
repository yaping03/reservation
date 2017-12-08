from django.shortcuts import render,redirect
from app01 import models
import json
# Create your views here.


def showtime(request):
    timer = models.Timer.objects.all()
    confe = models.Conference.objects.all()
    reserve=models.Date2Timer.objects.all()
    res_dict={}
    for i in reserve:
        res_dict[i.timer]=[i.confe.name,i.people.name]
    if request.method=="POST":
        data=json.loads(request.POST.get("commit"))
        pass
    return render(request,"showtime.html",{"timer":timer,"confe":confe,"res":res_dict})

def login(request):
    status = ""
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        obj = models.Student.objects.filter(user=user, pwd=pwd).first()
        if obj:
            print("not")
            request.session["msg"]={"user":obj.user,"cls":obj.cls.id,"id":obj.id}
            return redirect("/answer/1")
        else:
            status="用户名或密码错误"
    return render(request, "login.html",{"status":status})
