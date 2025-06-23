from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Item, Stock
from .forms import ItemForm, StockForm


def dashboard(request):
    return render(request, 'inventory/dashboard.html')


def pos(request):
    return render(request, 'inventory/pos.html')


def item_list(request):
    if request.method == 'POST' and 'name' in request.POST:
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Item added successfully.")
            return redirect('items')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
    else:
        form = ItemForm()

    items = Item.objects.all()
    return render(request, 'inventory/items.html', {'form': form, 'items': items})


def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        try:
            item.save()
            messages.success(request, "Item updated successfully.")
        except:
            messages.error(request, "Another item with this name already exists.")
    return redirect('items')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Item deleted successfully.")
    return redirect('items')


def stock(request):
    if request.method == 'POST':
        # Yeni stok ekleme formu gönderildi
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Stock added/updated successfully.")
            return redirect('stock')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
        stocks = Stock.objects.select_related('item').all()  # Hatalı formda yine tüm liste gelsin
    else:
        form = StockForm()
        query = request.GET.get('q')
        if query:
            stocks = Stock.objects.select_related('item').filter(
                Q(item__name__icontains=query) |
                Q(description__icontains=query)
            )
        else:
            stocks = Stock.objects.select_related('item').all()

    return render(request, 'inventory/stock.html', {
        'form': form,
        'stocks': stocks,
    })

from django.template.loader import render_to_string
from django.http import JsonResponse

def stock_search(request):
    query = request.GET.get('q', '')
    if query:
        stocks = Stock.objects.select_related('item').filter(
            Q(item__name__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        stocks = Stock.objects.select_related('item').all()

    html = render_to_string('inventory/_stock_table.html', {'stocks': stocks})
    return JsonResponse({'html': html})

from django.template.loader import render_to_string
from django.http import JsonResponse

def stock_search(request):
    query = request.GET.get('q', '')
    stocks = Stock.objects.select_related('item').filter(
        Q(item__name__icontains=query) |
        Q(description__icontains=query)
    ) if query else Stock.objects.select_related('item').all()

    html = render_to_string('inventory/_stock_table.html', {'stocks': stocks})
    return JsonResponse({'html': html})
