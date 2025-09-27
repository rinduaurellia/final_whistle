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

# Berisi logika yang akan ditampilkan pengguna (jembatan modls dan template)

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

# Form menambah produk baru 
def create_product(request):
    # Validasi input ssupaya produk terkait user login
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST": # Kirim data ke server
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
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
     return HttpResponse(xml_data, content_type="application/xml")

# Export semua produk dalam format JSON
def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

# Export 1 produk berdasarkan id
def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
   try:
       product_item = Product.objects.get(pk=product_id)
       json_data = serializers.serialize("json", [product_item])
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

# Registrasi akun baru
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

# Login user
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

# Logout user
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def show_hot_products(request):
    # Filter produk yang memiliki views lebih besar dari 50 dan diurutkan berdasarkan views tertinggi
    hot_products = Product.objects.filter(views__gt=50).order_by('-views') 
    
    context = {
        'nama_aplikasi': 'Final Whistle',
        'name': 'Rindu Aurellia Zahra',
        'class': 'PBP C',
        'product_list': hot_products, 
        'last_login': request.COOKIES.get('last_login', 'Never'),
        # BARIS INI HARUS DITAMBAHKAN
        'is_hot_page': True 
    }
    # Menggunakan template yang sama (main.html) untuk menampilkan daftar produk
    return render(request, "main.html", context)

