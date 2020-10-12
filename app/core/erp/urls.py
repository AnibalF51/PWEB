from django.urls import path
from core.erp.view.category.views import *
from core.erp.views import CategoryListView

app_name ='erp'

urlpatterns = [
 path('category/list/', CategoryListView.as_view(), name='category_list'),
   # path('dos/', mysecondview, name='vista2')
]