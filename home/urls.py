from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('problem_view/<pk>/',views.problem_view,name='problem_view_url'),
    path('editor/<pk>/',views.editor,name='editor'),
    path('handle_submissions/<pk>/',views.handle_submissions,name='handle_submissions'),
    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)