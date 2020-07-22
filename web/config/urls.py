"""
Definition of urls for TestWeb.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from web.app import views, forms

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/',
         LoginView.as_view
         (template_name='login.html',
          authentication_form=forms.BootstrapAuthenticationForm,
          extra_context={
              'title': 'Log in',
              'year': datetime.now().year,
          }
          ),
         name='signin'),
    path('todo/delete/<str:id>/', views.delete_todo, name='delete_todo'),
    path('todo/save/', views.save_todo, name='save_todo'),
    path('todo/<str:id>/', views.todo_form, name='todo_form'),
    path('todo/', views.todo_form, name='todo_form'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
