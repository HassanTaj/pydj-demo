"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from lib.uow.UnitOfWorkModule import *

def home(request):
    """Renders the home page."""
    uow: UnitOfWork = request.uow
    print('todos')
    t = Todo()
    # t.id =0
    t.task ='task'
    t.description ='desc'
    t.endDate ='1/1/1'

    # uow.todoRepo.create(t)
    print(len(uow.todoRepo.get_all()))

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )
