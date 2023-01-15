from django.forms import ModelForm
from .models import listings


class ListingForm(ModelForm):
    class Meta:
        model = listings
        fields = [
            "title",
            "price",
            "num_bedrooms",
            "num_bathrooms",
            "square_footage",
            "address" 
          

        ]