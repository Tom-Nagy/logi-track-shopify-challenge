''' Views for login and inventory management '''

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Item


def index(request):
    ''' Render the home page '''
    template = 'inventory/index.html'
    return render(request, template)


def user_login(request):
    ''' View to verify credentials and log the user in '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, 'Successfuly logged in')
            login(request, user)
            template = 'inventory/inventory_management.html'
            return render(request, template)
        else:
            messages.error(request, 'Incorrect credentials, try again')
            redirect(reverse('index'))
    else:
        if request.user.is_authenticated:
            template = 'inventory/inventory_management.html'
            return render(request, template)


def user_logout(request):
    ''' logout user '''
    logout(request)
    return redirect('home')


@login_required
def all_items(request):
    ''' Display all inventory items '''
    items = Item.objects.all()
    template = 'inventory/all_items.html'
    context = {
        'items': items,
    }
    return render(request, template, context)


@login_required
def add_item(request):
    ''' Add an item to the inventory '''
    template = 'inventory/add_item.html'
    return render(request, template)
