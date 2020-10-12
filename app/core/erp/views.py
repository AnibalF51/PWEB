
from django.views.generic import ListView
from django.shortcuts import render
from core.erp.models import Category, Product
# Create your views here.

def myfirstview(request):
    data = {
        'title': 'Listado de Categorias',
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', data)

class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'


    def get_queryset(self):
        return Category.objects.filter(name__startswith='y')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        #context['object_list'] = Product.objects.all()
        return context
