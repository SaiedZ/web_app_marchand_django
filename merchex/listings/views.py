# from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing
from listings.forms import BandForm, ContactUsForm, ListingForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.shortcuts import redirect


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
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
                )
            return redirect('email-sent')
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
                  'listings/contact.html',
                  {'form': form})


def email_sent(request):
    return render(request,
                  'listings/email_sent.html')


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request,
                  'listings/band_create.html',
                  {'form': form})


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            listing = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    return render(request,
                  'listings/listing_create.html',
                  {'form': form})


def band_change(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    return render(request,
                  'listings/band_change.html',
                  {'band': band})
