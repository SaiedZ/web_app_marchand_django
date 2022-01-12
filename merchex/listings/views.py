# from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from django.shortcuts import get_object_or_404


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  context={'bands': bands})


def band_detail(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    listings = Listing.objects.all()
    return render(request,
                  'listings/listings.html',
                  context={'listings': listings})


def contact(request):
    return render(request, 'listings/contact.html')
