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
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
import json
from django.http import JsonResponse
import requests



# Berisi logika yang akan ditampilkan pengguna (jembatan modls dan template)
# tes
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    products = Product.objects.all() if filter_type == "all" else Product.objects.filter(user=request.user)

    last_login_time = request.user.last_login
    formatted_last_login = last_login_time.strftime("%d %b %Y, %H:%M") if last_login_time else "Never"

    context = {
        'nama_aplikasi': 'Final Whistle',
        'name': 'Rindu Aurellia Zahra',
        'class': 'PBP C',
        'product_list': products,
        'last_login': formatted_last_login,
    }
    return render(request, "main.html", context)

# Form menambah produk baru secara otomatis ketika disumbit dari form
def create_product(request):
    # Validasi input supaya produk terkait user login
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
            'uploader_username': product.user.username if product.user else 'Anonymous',
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

def show_json_by_user_id(request, product_id):
    try:
        try : 
            user = User.objects.get(id=product_id)
        except User.DoesNotExist : 
            return JsonResponse([], safe=False)
        product_list = Product.objects.filter(user=user)
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
            'uploader_username': product.user.username if product.user else 'Anonymous',
        }
        for product in product_list
        ]
        return JsonResponse(data, safe=False)
    
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
    return HttpResponseRedirect(reverse('main:show_main'))

def show_hot_products_json(request):
    """Return only products with views > 20 as JSON."""
    hot_products = Product.objects.filter(views__gt=20).order_by('-views')
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'price': int(product.price),
            'is_featured': product.is_featured,
            'rating_product': int(product.rating_product),
            'size_product': product.size_product,
            'brand': product.brand,
            'views': int(product.views),
            'user_id': product.user_id,
            'uploader_username': product.user.username if product.user else 'Anonymous',
        }
        for product in hot_products
    ]
    return JsonResponse(data, safe=False)

def show_hot_products(request):
    # Ambil hanya produk dengan views > 20
    hot_products = Product.objects.filter(views__gt=20).order_by('-views')
    
    context = {
        'nama_aplikasi': 'Final Whistle',
        'name': 'Rindu Aurellia Zahra',
        'class': 'PBP C',
        'product_list': hot_products,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'is_hot_page': True,  # Bisa dipakai buat highlight tombol
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

@csrf_exempt
@require_POST
def edit_product_entry_ajax(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)

    product.name = strip_tags(request.POST.get("name"))
    product.description = strip_tags(request.POST.get("description"))
    product.category = request.POST.get("category")
    product.thumbnail = request.POST.get("thumbnail")
    product.price = request.POST.get("price") or 0
    product.stock = request.POST.get("stock") or 0
    product.brand = strip_tags(request.POST.get("brand"))
    product.is_featured = request.POST.get("is_featured") == 'on'

    product.save()

    return HttpResponse(b"EDITED", status=200)

@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id, user=request.user)
        product.delete()
        return JsonResponse({"status": "success", "message": "Product deleted successfully!"}, status=200)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)

    
@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Your account has been successfully created!',
                'redirect_url': reverse('main:login')  # ✅ Redirect ke halaman login
            }, status=201)
        else:
            errors = []
            for field, error_list in form.errors.items():
                for error in error_list:
                    errors.append(f"{field.capitalize()}: {error}")
            return JsonResponse({
                'status': 'error',
                'message': "Registration failed.",
                'errors': errors
            }, status=400)

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method.'
    }, status=405)

from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def login_ajax(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # 🔥 Ini penting — update last_login otomatis
            return JsonResponse({
                "message": "Login successful!",
                "redirect_url": "/"
            })
        else:
            return JsonResponse({
                "message": "Invalid username or password."
            }, status=400)

    return JsonResponse({"message": "Invalid request method."}, status=400)


def logout_ajax(request):
    logout(request)

    response_data = {
        'status': 'success',
        'message': '👋 You have been successfully logged out.',
        'redirect_url': reverse('main:login')
    }

    response = JsonResponse(response_data)
    response.delete_cookie('last_login')
    return response

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_product_flutter(request):
    if request.method != 'POST':
        return JsonResponse({"status": "error", "message": "Invalid method"}, 
                            status=400)

    try:
        data = json.loads(request.body)

        name = strip_tags(data.get("name", ""))
        description = strip_tags(data.get("description", ""))
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        price = data.get("price", 0)
        is_featured = data.get("is_featured", False)
        rating_product = data.get("rating_product", 0)
        size_product = data.get("size_product", "")
        brand = data.get("brand", "")
        views = data.get("views", 0)

        # user dari session
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({
                "status": "error", 
                "message": "User not authenticated"
            }, status=401)

        new_product = Product(
            name=name,
            description=description,
            category=category,
            thumbnail=thumbnail,
            price=price,
            is_featured=is_featured,
            rating_product=rating_product,
            size_product=size_product,
            brand=brand,
            views=views,
            user=user,
        )

        new_product.save()

        return JsonResponse({"status": "success", "message": "Product created"}, 
                            status=200)

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, 
                            status=500)
    
@login_required
def my_products_json(request):
    products = Product.objects.filter(user=request.user)

    return JsonResponse([
        {
            'id': str(p.id),
            'name': p.name,
            'description': p.description,
            'category': p.category,
            'thumbnail': p.thumbnail,
            'price': int(p.price),
            'is_featured': p.is_featured,
            'rating_product': int(p.rating_product),
            'size_product': p.size_product,
            'brand': p.brand,
            'views': int(p.views),
            'user_id': p.user_id,
            'uploader_username': p.user.username,
        }
        for p in products
    ], safe=False)