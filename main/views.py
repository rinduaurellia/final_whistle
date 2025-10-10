import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Berisi logika yang akan ditampilkan pengguna (jembatan modls dan template)
# tes
@login_required(login_url='/login')
# Menampilkan halaman utama daftar product tapi user harus login
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'
    # Menentukan produk mana yang akan ditampilkan
    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)
    
    context = {
        'nama_aplikasi': 'Final Whistle',
        'name': 'Rindu Aurellia Zahra',
        'class': 'PBP C',
        'product_list': products,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    # Menerima parameter request mengatur permintaan HTTP dan mengembalikan tampilan sesuai (menghubungan views dan template)
    return render(request, "main.html", context)

# Form menambah produk baru secara otomatis ketika disumbit dari form
def create_product(request):
    # Validasi input supaya produk terkait user login
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST": # Kirim data ke server
        product_entry = form.save(commit = False)
        product_entry.user = request.user 
        product_entry.save()
        messages.success(request, f"Product : '{product_entry.name}' berhasil dibuat.")
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

@login_required(login_url='/login')
# Menampilkan detail produk 
def show_product(request, id):
    # Cari produk berdasarkan id
    product = get_object_or_404(Product, pk=id)

    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

# Export semua produk dalam format XML
def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml") # Return HTTP respons dengan XML data ke prosuct_list

# Export semua produk dalam format JSON
def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id), # UUID harus menjadi string
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail, # URLField
            'price': int(product.price), # IntegerField
            'is_featured': product.is_featured,
            'rating_product': int(product.rating_product), # IntegerField
            'size_product': product.size_product,
            'brand': product.brand,
            'views': int(product.views), # PositiveIntegerField
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id), # UUID harus menjadi string
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail, # URLField
            'price': int(product.price), # IntegerField
            'is_featured': product.is_featured,
            'rating_product': int(product.rating_product), # IntegerField
            'size_product': product.size_product,
            'brand': product.brand,
            'views': int(product.views), # PositiveIntegerField
            'user_id': product.user_id,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

# DEMO 4
# Registrasi akun baru -> buat register html
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else : 
             messages.error(request, "Registration Failed. Try Again.")

    context = {'form':form}
    return render(request, 'register.html', context)

# Login user -> buat login html nya & set cookies ketika user login
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcomeback, {user.username}!")
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      else : 
            messages.error(request, "Login Failed. Check your username and password.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

# Logout user -> buat botton di main.html --> hapus cookie ketika user logout
def logout_user(request):
    logout(request)
    messages.info(request, "You're logged out, See You!")
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# DEMO 5 -> buat html nya dit emplates
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        messages.info(request, f"Product :  '{product.name}' successfully updated.")
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

# Hapus product, tambahkan di main html
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    messages.error(request, f"Produk '{product.name}' has been deleted.")
    return HttpResponseRedirect(reverse('main:show_main'))

def show_hot_products(request):
    # Filter produk yang memiliki views lebih besar dari 20 dan diurutkan berdasarkan views tertinggi
    hot_products = Product.objects.filter(views__gt=20).order_by('-views') 
    
    context = {
        'nama_aplikasi': 'Final Whistle',
        'name': 'Rindu Aurellia Zahra',
        'class': 'PBP C',
        'product_list': hot_products, 
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'is_hot_page': True 
    }
    return render(request, "main.html", context)

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    if not request.user.is_authenticated:
        return HttpResponse(b"UNAUTHORIZED", status=401)

    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    brand = request.POST.get("brand") 
    size_product = request.POST.get("size_product")
    is_featured = request.POST.get("is_featured") == 'on' 
    price_str = request.POST.get("price")
    price_val = int(price_str) if price_str and price_str.isdigit() else 0    
    rating_val = 0 
    if not brand or not size_product or price_val <= 0:
        return HttpResponse(b"MISSING_REQUIRED_FIELDS", status=400)

    new_product = Product(
        name=name, 
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        price=price_val,          
        brand=brand,
        size_product=size_product, 
        rating_product=rating_val,
                
        user=request.user
    )
    new_product.save()
    return HttpResponse(b"CREATED", status=201)

