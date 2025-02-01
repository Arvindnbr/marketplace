from django.shortcuts import render, get_object_or_404

from .models import ProductItems

# Create your views here.

def details(request, pk):
    item = get_object_or_404(ProductItems, pk=pk)
    related_items = ProductItems.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        "related": related_items,
    })
