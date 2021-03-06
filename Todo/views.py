from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm, UserForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def signup_user(request):
    if request.method == 'GET':
        return render(request, 'signup_user.html', {'form': UserForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],  password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('current_todos')
            except IntegrityError:
                return render(request, 'signup_user.html', {'form': UserForm(), 'error': "Username alresdy exist. Please choose a new username"})
        else:
            return render(request, 'signup_user.html', {'form': UserForm(), 'error' : "Password did not match"})

def login_user(request):
    if request.method == 'GET':
        return render(request, 'login_user.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'signup_user.html', {'form': AuthenticationForm(), 'error': "Username and Password does not match"})
        else:
            login(request, user)
            return redirect('current_todos')

@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def create_todos(request):
    if request.method == 'GET':
        return render(request, 'create_todos.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('current_todos')
        except ValueError:
            return render(request, 'create_todos.html', {'form': TodoForm(), 'error': "Bad data passed in. Try again"})

@login_required
def current_todos(request):
    todos = Todo.objects.filter(user=request.user, completed_date__isnull=True)
    return render(request, 'current_todos.html', {'todos': todos})

@login_required
def view_todos(request, todo_pk):
    todo = get_object_or_404(Todo, pk= todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'view_todos.html', {'todo': todo, 'form' : form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('current_todos')
        except ValueError:
            return render(request, 'view_todos.html', {'todo': todo, 'form': form, 'error': "Bad data passed in. Try again" })


@login_required
def complete_todos(request, todo_pk):
    todo = get_object_or_404(Todo, pk= todo_pk, user=request.user)
    if request.method == 'POST':
        todo.completed_date = timezone.now()
        todo.save()
        return redirect('current_todos')

@login_required
def delete_todos(request, todo_pk):
    todo = get_object_or_404(Todo, pk= todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('current_todos')

@login_required
def completed_todos(request):
    todos = Todo.objects.filter(user=request.user, completed_date__isnull=False).order_by('-completed_date')
    return render(request, 'completed_todos.html', {'todos': todos})