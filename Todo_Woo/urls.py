"""Todo_Woo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    # Auth
    path('signup/', views.signup_user, name='signup_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),

    #Todos
    path('createtodos/', views.create_todos, name='create_todos'),
    path('currenttodos/', views.current_todos, name='current_todos'),
    path('todo/<int:todo_pk>', views.view_todos, name='view_todos'),
    path('todo/<int:todo_pk>/completetodos', views.complete_todos, name='complete_todos'),
    path('todo/<int:todo_pk>/deletetodos', views.delete_todos, name='delete_todos'),
    path('completedtodos/', views.completed_todos, name='completed_todos'),

]




