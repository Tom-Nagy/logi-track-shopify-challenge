'''Create and configure the item form'''

from django import forms

from .models import Item, Category, ItemStatus, Location


class ItemForm(forms.ModelForm):
    '''Configure the item form to add/edit products'''
    class Meta:
        ''' Form meta properties '''
        model = Item
        fields = ('category', 'name', 'friendly_name', 'sku', 'description',
                  'quantity', 'location', 'status',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Replace the categorie select box to see the friendly name.
        categories = Category.objects.all()
        categories_selection = []
        for category in categories:
            categories_selection.append(category)
        friendly_names = \
            [(c.id, c.get_friendly_name()) for c in categories_selection]
        self.fields['category'].choices = friendly_names

        # Replace the location select box to see the friendly name.
        locations = Location.objects.all()
        locations_selection = []
        for location in locations:
            locations_selection.append(location)
        friendly_names = \
            [(l.id, l.get_friendly_name()) for l in locations_selection]
        self.fields['location'].choices = friendly_names

        # Replace the ItemStatus select box to see the friendly name.
        item_status = ItemStatus.objects.all()
        status_selection = []
        for status in item_status:
            if status.name != "deleted":
                status_selection.append(status)
        friendly_names = \
            [(s.id, s.get_friendly_name()) for s in status_selection]
        self.fields['status'].choices = friendly_names
