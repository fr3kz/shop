from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    contex = {
        'listings': listings
    }

    return render(request,"pages/index.html", contex)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)[:1]
    context = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtors
    }
    return render(request,"pages/about.html",context)