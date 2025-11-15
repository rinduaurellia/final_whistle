from django.urls import path, include # definisikan urls
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product
from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id, delete_product, show_hot_products
from main.views import add_product_entry_ajax,edit_product_entry_ajax,delete_product_ajax,register_ajax,login_ajax,logout_ajax, show_hot_products, show_json_by_user_id, proxy_image, create_product_flutter,my_products_json

app_name = 'main'

# Konfigurasi rooting untuk aplikasi main
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create/', create_product, name='create_product'),
    path('<uuid:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/delete/', delete_product, name='delete_product'),  
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('create-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('edit-product-ajax/<uuid:id>/', edit_product_entry_ajax, name='edit_product_entry_ajax'),
    path('delete-product-ajax/<uuid:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('login-ajax/', login_ajax, name='login_ajax'),
    path('logout-ajax/', logout_ajax, name='logout_ajax'),
    path('edit-product-ajax/<uuid:id>/', edit_product_entry_ajax, name='edit_product_entry_ajax'),
    path('hot-products/', show_hot_products, name='show_hot_products'),
    path('json/<int:product_id>/product-user', show_json_by_user_id, name='show_json'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_product_flutter, name='create_news_flutter'),
    path("my-products-json/", my_products_json, name="my_products_json"),

    ]
