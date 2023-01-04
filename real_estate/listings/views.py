from django.shortcuts import render
from .models import listings
# Create your views here.
def listing_list(request):
    listing = listings.objects.all()
    context={
        "listing": listing,
    }

    return render(request, "listings.html", context = context)



def listing_retrieve(request, pk):
    listing=listings.objects.get(id=pk)
    context={
        "listing": listing,
    }
    return render(request, "listing.html", context = context)
