from django.contrib import admin
from listings.models import Band, Listing

# Register your models here.


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')


admin.site.register(Band, BandAdmin)


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'year', 'sold')


admin.site.register(Listing, ListingAdmin)
