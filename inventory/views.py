''' Views for login and inventory management '''

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Item, DeletedItem, ItemStatus
from .forms import ItemForm, DeletedItemForm


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
    if request.method == 'POST':
        item_form = ItemForm(request.POST, request.FILES)
        if item_form.is_valid():
            item_form.save()
            messages.success(request, 'Item added to the inventory')
            return redirect(reverse(all_items))
        else:
            messages.error(request, 'Fail to add item.'
                                    'Please ensure the form is valid.')
    else:
        item_form = ItemForm()
    template = 'inventory/add_item.html'
    context = {
        'item_form': item_form,
    }
    return render(request, template, context)


@login_required
def edit_item(request, item_id):
    ''' Edit an item in the inventory '''
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item_form = ItemForm(request.POST, request.FILES, instance=item)
        if item_form.is_valid():
            item_form.save()
            messages.success(request, 'Item edited successfuly')
            return redirect(reverse(all_items))
        else:
            messages.error(request, 'Fail to edit item.'
                                    'Please ensure the form is valid.')
    else:
        item_form = ItemForm(instance=item)
        messages.info(request, 'You are editing {item.friendly_name}')

    template = 'inventory/edit_item.html'
    context = {
        'item_form': item_form,
        'item': item,
    }
    return render(request, template, context)


@login_required
def item_deletion(request, item_id):
    ''' Delete an item from the inventory and create deleted_item '''
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        deletion_form = DeletedItemForm(request.POST, request.FILES)
        if deletion_form.is_valid():
            deleted_item = deletion_form.save(commit=False)
            user = request.user
            deleted_item.deleting_user = user
            # update the item status and save the item
            item_status = ItemStatus.objects.get(name='deleted')
            item.status = item_status
            item.save()

            deleted_item.item = item
            deleted_item.save()
            messages.success(request, 'Item successfuly deleted')
            return redirect(all_items)

    else:
        deletion_form = DeletedItemForm()

    template = 'inventory/item_deletion.html'
    context = {
        'item': item,
        'deletion_form': deletion_form,
    }
    return render(request, template, context)


@login_required
def deleted_items(request):
    ''' Display the deleted item '''
    items_deleted = DeletedItem.objects.all()
    template = 'inventory/deleted_items.html'
    context = {
        'items_deleted': items_deleted,
    }
    return render(request, template, context)


@login_required
def final_deletion(request, item_id):
    ''' Delete an item from the dadabase '''
    item_to_deleted = get_object_or_404(Item, pk=item_id)
    item_to_deleted.delete()
    messages.success(request, 'Item successfuly deleted')

    return redirect(reverse('deleted_items'))


@login_required
def restock_item(request, item_id):
    ''' re-stock a deleted item in the inventory '''
    item_to_restock = get_object_or_404(Item, pk=item_id)
    # update the item status and save the item
    item_status = ItemStatus.objects.get(name='stored')
    item_to_restock.status = item_status

    deleted_item = DeletedItem.objects.get(item=item_to_restock)
    item_to_restock.save()
    deleted_item.delete()
    messages.success(request, 'Item successfully restocked')
    return redirect(reverse('deleted_items'))
