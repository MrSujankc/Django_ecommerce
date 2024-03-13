
from product import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, SearchView, home
app_name = "product"

urlpatterns = [
    path('', home, name='home'),
    path('', views.Base, name='base'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('product/search', SearchView.as_view(), name = 'search-item'),
    path('signup/', views.SignUpView.as_view(), name='sign-up'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)