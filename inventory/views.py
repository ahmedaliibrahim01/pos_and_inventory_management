from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def dashboard(request):
    return render(request, 'inventory/dashboard.html')

def stock(request):
    return render(request, 'inventory/stock.html')

def pos(request):
    return render(request, 'inventory/pos.html')

def item_list(request):
    if request.method == 'POST' and 'name' in request.POST:
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items')
    else:
        form = ItemForm()

    items = Item.objects.all()
    return render(request, 'inventory/items.html', {'form': form, 'items': items})

def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.save()
    return redirect('items')
