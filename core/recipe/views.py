from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def blank(request):
    return render(request, 'base.html')

@login_required(login_url='/login')
def recipe(request):
    if request.method=='POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        recipe_img = request.FILES.get('recipe_img')
        
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_desc = recipe_desc,
            recipe_img = recipe_img
        )
        return redirect('/recipe')
        
    queryset = Recipe.objects.all()
    context = {'recipes': queryset}
        
    return render(request, 'recipe.html', context=context)


def update_recipe(request, id):
    queryset = Recipe.objects.get(id= id)
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        recipe_img = request.FILES.get('recipe_img')
    
        queryset.recipe_name = recipe_name
        queryset.recipe_desc = recipe_desc
        if recipe_img:
            queryset.recipe_img = recipe_img
            
            
        queryset.save()


    context = {'recipe': queryset}

    
    return render(request, "update.html", context=context)
    

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipe')
    # print(id)
    # return HttpResponse('a')
    
    
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # user = User.objects.filter(username = username)
        
        if User.objects.filter(username = username).exists():
            messages.info(request, 'User already exist')
            return redirect('/register')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        
        user.set_password(password)
        user.save() 
        
        messages.info(request, 'Account created')
        
    return render(request, 'register.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, 'invalid username')
            return redirect('/login')
        
        user = authenticate(request, username = username, password=password)
        
        if user:
            login(request, user)
            messages.info(request, 'Log in complete')
            return redirect('/recipe')
          
        else:
            messages.info(request, 'Incorrect password')
            return redirect('/login')   
            # return HttpResponse('fuck')
        
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login')


def about(request):
    return render(request, 'about.html')