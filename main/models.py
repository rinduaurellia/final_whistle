import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
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
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    price = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    rating_product = models.IntegerField()
    size_product = models.CharField(max_length=10)
    brand = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()