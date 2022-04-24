from django.shortcuts import render,HttpResponse
# Create your views here.
def home(request):
   # return HttpResponse(" HOMEPAGE(will be displaying whenever somebody)")
   #context={'name':'surbhi','course':'django'}
   return render(request,'home.html')
def about(request):
    return HttpResponse(" About us")
def contact(request):
    return render(request,'contact.html')


