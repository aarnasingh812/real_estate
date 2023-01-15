from django.shortcuts import render
from .models import listings
from .forms import ListingForm


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


def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form=ListingForm(request.POST)
        print(request.POST)
        if form.is_valid():

            pass
    context={
        "form": form
    }
    return render(request,"listing_create.html", context = context)
    
    
    