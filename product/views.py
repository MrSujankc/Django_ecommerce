from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



def home(request):
    # Your logic for the home view
    return render(request, 'product/home.html')



def Base(request):
    return render(request, 'product/base.html')

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/add_product.html'
    fields = '__all__'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/update_product.html'
    fields = '__all__'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('product-list')


class SearchView(ListView):
    model = Product
    template_name = "product/search.html"
    context_object_name = "products"
    
    def get_queryset(self):
        name = self.request.GET.get("name", "")
        return self.model.objects.filter(name__contains=name)
   
   
   
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"   
    success_url = reverse_lazy ("login")



   

