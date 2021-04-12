from django.shortcuts import render
from .models import *
from .math import *
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q  
# Create your views here.

from django import forms
      
def home1(request):
    posts = []
    for post in Interesting.objects.all():
        posts.append(preview.objects.get(pk=post.post_id))
    data = { 'prev':posts,'title':""}
    return render(request,'med/home1.html',data)

def home2(request):
    posts = []
    for post in Interesting.objects.all():
        posts.append(preview.objects.get(pk=post.post_id))
    data = { 'prev':posts,'title':""}
    return render(request,'med/home2.html',data)

def home3(request):
    posts = []
    for post in Interesting.objects.all():
        posts.append(preview.objects.get(pk=post.post_id))
    data = { 'prev':posts,'title':""}
    return render(request,'med/home3.html',data)

def index(request):
    posts = []
    for post in Interesting.objects.all():
        posts.append(preview.objects.get(pk=post.post_id))
    data = { 'prev':posts,'title':""}
    return render(request,'med/index.html',data)

def post(request,pk):
    try:
        post=preview.objects.get(pk=pk)
    except:
        raise Http404("Post does not exist")
      
    
    return render(
        request,
        'med/preview.html',
        context={'prev':post,}
    )

@csrf_exempt
def login_auth(request):
        error = ""
        if request.method != "POST":             
            return render(request, 'med/login.html', context= { 'error':error})
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        print(request.POST)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username, password)
       
        if username is None or password is None:
            return render(request, 'med/login.html', locals())
        else:
            Newuser = authenticate(username=username, password=password)
        if Newuser is not None:
            if Newuser.is_active:
                login(request,Newuser)
                return HttpResponseRedirect("/")
            else:
                error = "Ошибка аутентификации пользователя"
                return render(request, 'med/login.html', context= { 'error':error})
        else:
            error = "Неправильный логин или пароль"
            return render(request, 'med/login.html', context= { 'error':error})
        
def profile_views(request): 
    user = User.objects.get(username=request.user)   
    kkal = get_calories(user.profile);
    data = { 'rate':get_rate(user.profile.activity),'calories': kkal,'menyu':getMenyu(kkal),'gender':get_gender(user.profile.gender),'activ':get_activity(user.profile.activity),'target':get_target(user.profile.target)}
    return render(request, 'med/profile.html', data )


def update_profile(request, username):
    if request.method == "POST":
        user = User.objects.get(username=username)   
        user.profile.gender = request.POST.get('gender', None)
        user.profile.age = request.POST.get('age', None)
        user.profile.activity = request.POST.get('activity', None)
        user.profile.weight = request.POST.get('weight', None) 
        user.profile.height = request.POST.get('height', None)
        user.profile.target = request.POST.get('target', None)
        user.profile.steps = request.POST.get('steps', None)
        user.first_name = request.POST.get('firstName', None)
        user.last_name = request.POST.get('lastName', None)
        user.email  = request.POST.get('email', None)
        user.save()

def update_profile_user(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)   
        user.profile.age = request.POST.get('age', None) 
        user.profile.weight = request.POST.get('weight', None) 
        user.profile.height = request.POST.get('height', None) 
        user.profile.steps = request.POST.get('steps', None)
        user.save()
        return HttpResponseRedirect('/')
      
def register(request):
    if request.user.is_authenticated:
            return HttpResponseRedirect('/')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
           user = form.save() 
           login(request, user)
           update_profile(request, user)
           return HttpResponseRedirect('/')
        else:
            return render(request=request,template_name="med/registration.html",context= { 'error':form.errors})
    return render(request=request,template_name="med/registration.html",context= { 'error':""})
@csrf_exempt
def logout_auth(request): 
 logout(request)
 return HttpResponseRedirect('/')
