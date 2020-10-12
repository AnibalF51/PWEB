
from django.views.generic import ListView
from django.shortcuts import render
from core.erp.models import Category, Product
# Create your views here.

def myfirstview(request):
    data = {
        'name': 'RAIDER',
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', data)

class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'