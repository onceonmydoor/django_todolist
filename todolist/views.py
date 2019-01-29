from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def home(request):
    if request.method == "POST":
        if request.POST['待办事项'] =="":
            conent={'清单':Todo.objects.all(),'警告':"请输入内容!"}
            return render(request,"todolist/home.html",conent)
        else:
            a_row = Todo(thing=request.POST['待办事项'],done=False)
            a_row.save() #一定要保存才能存入数据
            conent={'清单':Todo.objects.all(),'信息':"添加成功!"}
            return render(request,"todolist/home.html",conent)
    elif request.method == "GET":
        conent={'清单':Todo.objects.all()}
        return render(request,"todolist/home.html",conent)
    #运送网页
def about(request):
    return render(request,"todolist/about.html")
    #重新渲染界面，运送（网址）

def edit(request,eachthing_id):
    a=Todo.objects.get(id=eachthing_id)
    content = {"change":a.thing}
    if request.method == "POST":
        if request.POST['changetodo'] =="":
            return render(request,"todolist/edit.html",{'警告':"请输入内容!"})
        
        a.thing=request.POST["changetodo"]
        a.save()
        return redirect("todolist:主页")
    elif request.method == "GET":
        content = {"change":a.thing}
        return render(request,"todolist/edit.html",content)
def delete(request,eachthing_id):
    #跳转到主页(网页)
    a=Todo.objects.get(id=eachthing_id)
    a.delete()
    return redirect("todolist:主页")
def cross(request,eachthing_id):
    if request.POST["state"] == "done":
        a=Todo.objects.get(id=eachthing_id)
        a.done =True
        a.save()
        return redirect("todolist:主页")
    else:
        a=Todo.objects.get(id=eachthing_id)
        a.done =False
        a.save()
        return redirect("todolist:主页")
