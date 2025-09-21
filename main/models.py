import uuid
from django.db import models
from django.contrib.auth.models import User

# Mengatur struktur data produk di database, mendefinisikan model
class Product(models.Model):
    # Relasi produk - user (many-to-one)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('update', 'Update'),
        ('jersey', 'Jersey'),
        ('sepatu', 'Shoes'),
        ('aksesoris', 'Accessories'),
        ('topi', 'Hat'),
        ('ball', 'Football'),
        ('kaos_kaki', 'Socks'),
    ]
    
    # Field yang harus dimiliki setiap product
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True) # Boleh kosong di form atau database
    price = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    rating_product = models.IntegerField()
    size_product = models.CharField(max_length=10)
    brand = models.CharField(max_length=30)
    views = models.PositiveIntegerField(default=0)    

    # Mengatur string representasi objek
    def __str__(self):
        return self.title
    
    @property
    def is_product_hot(self):
        return self.views > 20
        
    def increment_views(self):
        self.views += 1
        self.save()