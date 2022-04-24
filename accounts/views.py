from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import logout,login,authenticate


# Create your views here.
def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                print('Email Taken')
                return redirect('register')
                
            else:
                User.objects.create_user(name=name,email=email,password=password1)
                print('User Created')
                return redirect('signin') # name of URL Path
        else:
            messages.info(request,'password not matching')
            print('password not matching')
            return redirect('register')
        
    else:
        return render(request,'register.html')

def signin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        User = get_user_model()

        # if User.DoesNotExist:
        #     messages.info(request,'user does not exist')
        #     return redirect('login')
       # else:
        if password:
            usera=authenticate(request,email=email,password=password)
            # if user.check_password(password):
            if usera is not None:
                    login(request,usera)
                    return redirect("/")
            else:
                try:
                    user=User.objects.get(email=email)
                except User.DoesNotExist:
                    print('USER does not exist')
                    messages.info(request,'User does not exist')
                    return redirect('register')
                else:    
                    messages.info(request,'password incorrect')
                    return redirect('signin')

    else:
        return render(request,'login.html')

def signout(request): # keeping the nsmae signout as it was giving runtime error max recursion depth reached, it waskeep calling itself
    logout(request)
    return redirect('/')