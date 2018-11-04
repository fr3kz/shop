from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Listing
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings,1)
    page = request.GET.get('page')
    paged_list = paginator.get_page(page)

    contex = {
        'listings':paged_list
    }

    return render(request,'listings/listings.html',contex)

def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html',context)

def search(request):
    return render(request, 'listings/search.html')
