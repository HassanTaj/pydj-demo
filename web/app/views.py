"""
Definition of views.
"""
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.decorators.http import *

from lib.uow.UnitOfWorkModule import *


def home(request):
    """Renders the home page."""
    uow: UnitOfWork = request.uow

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'todos': uow.todoRepo.get_all()
        }
    )


@require_GET
def todo_form(request, id=None):
    uow: UnitOfWork = request.uow
    todo = None
    if id is not None and id != '':
        todo = uow.todoRepo.get_by_id(id)

    return render(
        request,
        'todo_form.html', {
            'title': 'Todo Page',
            'todo': todo
        }
    )


@require_POST
def save_todo(request):
    """
        Method is Used to CREATE or UPDATE a database entity
        it checks if the id is none if it is then it's a new record otherwise it would be an update call
    """
    uow: UnitOfWork = request.uow
    todo: Todo = Todo(
        id=request.POST['id'],
        task=request.POST['task'],
        description=request.POST['description'],
        endDate=request.POST['dueDate']
    )
    print(todo.id)
    if todo.id is not None and todo.id != '':
        uow.todoRepo.update(todo.id, todo)
    else:
        todo.id = None
        uow.todoRepo.create(todo)
    return redirect('/')


def delete_todo(request, id):
    uow: UnitOfWork = request.uow
    if id is not None:
        uow.todoRepo.delete(Todo(id=id))
    return redirect('/')
