from urllib import response
from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact,Problems,Solutions
from django.contrib.auth import get_user_model
from django.contrib.auth import logout,login,authenticate
from django.conf import settings
from django.core.files.base import File
from datetime import date,datetime
import json
from home.utility.api_utils import get_languages,languages,create_submissions

# Create your views here.
User=get_user_model()
def home(request):
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
        problem=Problems.objects.prefetch_related('testcases').get(id=problem_id)#query set api
        testcases=problem.testcases.all()
        print(testcases)
        if request.method=="POST":
                editor=request.POST.get('code') # line 67,68,69 outside loop
                language=request.POST.get('language')
                print(editor,problem.name,problem.id,language,problem)
                count=0
                tc_count=0
                for tc in testcases:
                    tc_count=tc_count+1
                    with open(f'{settings.MEDIA_ROOT}/{tc.testcase}',"r+") as file:
                        arr = file.readlines()
                        arr = [x.strip('\n') for x in arr]
                        input_part=arr[0].split('=')[1]
                        output_part=arr[1].split('=')[1]
                        print(input_part,output_part)
                        print(editor,problem.name,problem.id,language,problem) 
                    try:
                        submission=create_submissions(code=editor,language=language,stdin=input_part)
                        print(submission)
                        file_name=get_file_name(str(problem.id),request.user)
                        with open(f"{settings.MEDIA_ROOT}/{file_name}.txt","w+") as file:
                            file.write(editor)
                            user_email=request.user.email
                            user=User.objects.get(email=user_email)
                            status=submission.get("status")
                            verdict=status.get("description")
                            output=submission.get("stdout")
                            output = output.strip('\n')
                            if(verdict=="Accepted"):
                                print(output_part,output)
                                if(output_part==output):
                                    count=count+1  
                            # solution.save()
                            # print(f'no of tc passed {count}')
                    except Exception as e:
                        print(e)
                # if(count==tc_count):
                #     test_verdict="Accepted"
                # else:
                #     test_verdict="Rejected"
                test_verdict="Accepted" if count==tc_count else "Rejected"
                Solutions.objects.create(problem=problem,user=user,language=language,
                            code_file_path=f"{settings.MEDIA_ROOT}code/{file_name}.txt",verdict=test_verdict)
                print(f'no of tc passed {count} out of {tc_count}')
                # return redirect(request,'submission_result.html',) 
                data={
                    "test_case_passed": count,
                    "total_test_case": tc_count,
                    "verdict":test_verdict,
                }
                return HttpResponse(json.dumps(data),status=200,content_type="text/plain") 
    else:
        return redirect(request,'login.html')


