from django.shortcuts import render,redirect,HttpResponse
from app01 import models
import json
# Create your views here.


def showtime(request):
    msg = request.session.get("msg")
    if not msg:
        return redirect("/login")
    date = request.GET.get("date")
    if date:
        day, month, year = date.split(" ")
        date_obj = models.Date.objects.filter(date__year=year,date__month=month,date__day=day).first()
        if not date_obj:
            date_obj=models.Date.objects.create(date="%s-%s-%s"%(year,month,day))
    name = msg.get("name")
    user = msg.get("user")
    timer = models.Timer.objects.all()
    confe = models.Conference.objects.all()
    if not date:
        reserve=models.Date2Timer.objects.filter(date_id=1)
    else:
        reserve = models.Date2Timer.objects.filter(date=date_obj)
    res_dict={}
    for i in reserve:
        if not res_dict.get(i.timer):
            res_dict[i.timer]={i.confe.name:i.people.name}
        else:
            res_dict[i.timer][i.confe.name]=i.people.name
    if request.method=="POST":
        print("预定")
        date = request.POST.get("date")
        if date:
            day, month, year = date.split(" ")
            date_obj = models.Date.objects.filter(date__year=year, date__month=month, date__day=day).first()
            if not date_obj:
                date_obj = models.Date.objects.create(date="%s-%s-%s" % (year, month, day))
        if request.POST.get("commit"):
            data=json.loads(request.POST.get("commit"))
            for item in data:
                conference=models.Conference.objects.filter(name=item[0]).first()
                people = models.People.objects.filter(user=user).first()
                time = models.Timer.objects.filter(id=int(item[1])).first()
                if not date:
                    models.Date2Timer.objects.create(confe=conference,date_id=1,people=people,timer=time)
                else:
                    models.Date2Timer.objects.create(confe=conference, date=date_obj, people=people, timer=time)
        if request.POST.get("dellist"):
            del_list = data=json.loads(request.POST.get("dellist"))
            for item in del_list:
                conference=models.Conference.objects.filter(name=item[0]).first()
                people = models.People.objects.filter(user=user).first()
                time = models.Timer.objects.filter(id=int(item[1])).first()
                if not date:
                    models.Date2Timer.objects.filter(confe=conference,date_id=1,people=people,timer=time).delete()
                else:
                    models.Date2Timer.objects.filter(confe=conference,date=date_obj,people=people,timer=time).delete()
        print("成功")
        return HttpResponse("ok")
    if not date:
        date = "09 12 2017"
    return render(request,"showtime.html",{"timer":timer,"confe":confe,"res":res_dict,"name":name,"date":date})

def login(request):
    status = ""
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        obj = models.People.objects.filter(user=user, pwd=pwd).first()
        if obj:
            request.session["msg"]={"user":obj.user,"name":obj.name}
            return redirect("/showtime/")
        else:
            status="用户名或密码错误"
    return render(request, "login.html",{"status":status})