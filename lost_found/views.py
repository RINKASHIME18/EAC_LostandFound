from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout as django_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .models import Item

# 1. HOME VIEW
def home(request):
    lost_items = Item.objects.filter(status='Lost').order_by('-date_reported')
    found_items = Item.objects.filter(status='Found').order_by('-date_reported')
    return render(request, 'lost_found/home.html', {
        'lost_items': lost_items, 
        'found_items': found_items
    })

# 2. SEARCH VIEW
def search_results(request):
    query = request.GET.get('q', '')
    location = request.GET.get('location', '')
    category = request.GET.get('category', '')
    date_lost = request.GET.get('date_lost', '')

    items = Item.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query) | Q(category__icontains=query),
        location__icontains=location
    )

    if category:
        items = items.filter(category=category)
    
    if date_lost:
        items = items.filter(date_lost=date_lost)

    return render(request, 'lost_found/home.html', {
        'lost_items': items.filter(status='Lost'),
        'found_items': items.filter(status='Found')
    })

def logout_view(request):
    if request.method == 'POST':
        django_logout(request)
        return redirect('home')
    return redirect('home')

def is_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

from django.contrib.auth.decorators import user_passes_test


@login_required
def report_lost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        location = request.POST.get('location')
        description = request.POST.get('description')
        date_lost = request.POST.get('date_lost')
        time_lost = request.POST.get('time_lost')
        images = request.FILES.getlist('images')

        item = Item.objects.create(
            title=title,
            category=category,
            location=location,
            description=description,
            date_lost=date_lost,
            time_lost=time_lost,
            status='Lost',
            user=request.user  # Associate with logged-in user
        )

        for img in images:
            ItemImage.objects.create(item=item, image=img)
        messages.success(request, "Lost item reported successfully!")
        return redirect('home')
        
    return render(request, 'lost_found/lost_item.html')

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    
    # Only allow staff to delete items
    if request.user.is_staff:
        item.delete()
        messages.success(request, "Item deleted successfully.")
    else:
        messages.error(request, "Only administrators can delete items.")
        
    return redirect('home')

@login_required
def report_found(request):
    lost_items = Item.objects.filter(status='Lost').order_by('-date_reported')
    found_items = Item.objects.filter(status='Found').order_by('-date_reported')
    return render(request, 'lost_found/found_item.html', {
        'lost_items': lost_items,
        'history_items': found_items
    })


@user_passes_test(is_admin)
def mark_as_found(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.status = 'Found'
    item.save()
    messages.info(request, "Item status updated to Found.")
    return redirect('report_found')

def lost_found_view(request):
    items = Item.objects.all().order_by('-date_posted')
    return render(request, 'index.html', {'items': items})

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        user = authenticate(request, username=u, password=p)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Mali ang Username o Password!")
    return render(request, 'lost_found/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'lost_found/register.html', {'form': form})


@login_required
def messages_view(request):
    return render(request, 'lost_found/messages.html')

def about(request):
    return render(request, 'lost_found/about.html')

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'lost_found/item_detail.html', {'item': item})
