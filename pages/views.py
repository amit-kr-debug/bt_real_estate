from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]

    context = {
        'listings': listings
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.all()
    realtor_of_month = Realtor.objects.filter(is_mvp = True)[0]
    context = {
        'realtors': realtors,
        'mvp': realtor_of_month
    }
    return render(request, 'pages/about.html', context)
