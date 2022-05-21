from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact,Problems
from django.contrib.auth import get_user_model
from django.contrib.auth import logout,login,authenticate
import sys
from django.conf import settings
from django.core.files.base import File
from datetime import date,datetime

from home.utility.api_utils import get_languages,languages,create_submissions

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
    # print(request.user,request.user.is_authenticated)
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
def get_file_name(p_id,user_email):
    current_date=str(date.today())
    time=datetime.now()
    time=time.strftime("%H-%M-%S")
    file_name=(f"{current_date}_{time}_{p_id}_{user_email}")
    return file_name

def handle_submissions(request,pk): 
    if request.user.is_authenticated:
        problem_id=int(pk)
        problem=Problems.objects.get(id=problem_id)
        if  request.method=="POST":
            # editor=request.POST['editor']
            editor=request.POST.get('code')
            language=request.POST.get('language')
            # print(request.POST)
            print(editor,problem.name,problem.id,language,problem)
            # TODO:save data into db and check for many to many from user and solutions 
            try:
                languages=get_languages()
                submission=create_submissions(code=editor,language=language)
                print(submission)
                file_name=get_file_name(str(problem.id),request.user)
                with open(f"{settings.MEDIA_ROOT}/{file_name}.txt","w+") as file:
                    file.write(editor)
                # orig_stdout= sys.stdout
                # sys.stdout=open('file.txt','w')
                # exec(editor)
                # sys.stdout.close()
                # sys.stdout=orig_stdout
                # output=open('file.txt','r').read()
                
            except Exception as e:
                # sys.stdout.close()
                # sys.stdout=orig_stdout
                # output=e
                pass
            

            return HttpResponse("yess")  
    else:
        return redirect(request,'login.html')

