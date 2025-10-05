from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags


# Form dan fields untuk model Product
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
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
        
