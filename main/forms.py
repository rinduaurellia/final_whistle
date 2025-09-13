from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "category",
            "thumbnail",
            "price",
            "is_featured",
            "rating_product",
            "size_product",
            "brand"
        ]
