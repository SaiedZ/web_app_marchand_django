# from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from django.shortcuts import get_object_or_404


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})


def band_detail(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})


def band_listing(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    return render(request,
                  'listings/band_listing_list.html',
                  {'band': band})


def about(request):
    return render(request, 'listings/about.html')


def listings_list(request):
    listings = Listing.objects.all()
    return render(request,
                  'listings/listings_list.html',
                  context={'listings': listings})


def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request,
                  'listings/listing_detail.html',
                  context={'listing': listing})


def contact(request):
    return render(request, 'listings/contact.html')
