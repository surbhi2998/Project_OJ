from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact,Problems
from django.contrib.auth import get_user_model
from django.contrib.auth import logout,login,authenticate
# Create your views here.
User=get_user_model()
def home(request):
   # return HttpResponse(" HOMEPAGE(will be displaying whenever somebody)")
    if request.method=="GET":
        problems = Problems.objects.all()
        return render(request,'home.html',{'problems': problems})

def problem_view(request,pk):
    problem_id=int(pk)
    problem=Problems.objects.get(id=problem_id)
    if request.method=="GET":
        return render(request,'problemdetail.html',{'problem': problem})
def about(request):
    return HttpResponse(" About us")
def editor(request,pk):
    print(request.user,request.user.is_authenticated)
    if request.user.is_authenticated:
        problem_id=int(pk)
        problem=Problems.objects.get(id=problem_id)
        return render(request,'editor.html',{'problem': problem})
    else:
        return render(request,'login.html')   
    
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        print(name,email,phone,desc)
        ins= Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
        print("in db")
    return render(request,'contact.html')
def handle_submissions(request,pk):
    
    if request.user.is_authenticated:
        problem_id=int(pk)
        problem=Problems.objects.get(id=problem_id)
        if request.method=="POST":
            editor=request.POST['editor']
            print(editor,problem.name,problem.id)
            return HttpResponse("yess")  
    else:
        return redirect(request,'login.html')

