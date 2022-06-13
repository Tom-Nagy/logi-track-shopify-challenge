''' Admin configuration and registration for inventory app '''

from django.contrib import admin
from .models import Item, Category, Location, ItemStatus


class LocationAdmin(admin.ModelAdmin):
    ''' Allow access to Location from admin '''

    model = Location()

    list_display = ('name', 'friendly_name',)


class ItemStatusAdmin(admin.ModelAdmin):
    ''' Allow access to ItemStatus from admin '''

    model = ItemStatus()

    list_display = ('name', 'friendly_name',)


class CategoryAdmin(admin.ModelAdmin):
    ''' Allow access to ItemStatus from admin '''

    model = Category()

    list_display = ('name', 'friendly_name',)


class ItemAdmin(admin.ModelAdmin):
    ''' Customise the admin Item interface '''

    model = Item()

    list_display = (
        'name',
        'category',
        'quantity',
        'location',
        'status',
        'date_added',
        'sku',
    )

    ordering = ('location', 'category',)


# Models registration with relevant classes
admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ItemStatus, ItemStatusAdmin)
admin.site.register(Location, LocationAdmin)
