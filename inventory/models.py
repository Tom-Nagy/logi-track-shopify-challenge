''' Models configuration for Inventory app '''

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ItemStatus(models.Model):
    ''' Model that define how the data will be store for ItemStatus '''

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        ''' String method to return the name of the ItemStatus '''
        return str(self.name)

    def get_friendly_name(self):
        ''' String method to return the firendly name of the ItemStatus '''
        return str(self.friendly_name)


class Location(models.Model):
    ''' Model that define how the data will be store for a location '''

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        ''' String method to return the name of the location '''
        return str(self.name)

    def get_friendly_name(self):
        ''' String method to return the firendly name of the location '''
        return str(self.friendly_name)


class Category(models.Model):
    ''' Model that define how the data will be store for a category '''
    class Meta:
        ''' Set plural verbose name '''
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        ''' String method to return the name of the category '''
        return str(self.name)

    def get_friendly_name(self):
        ''' String method to return the firendly name of the category '''
        return str(self.friendly_name)


class Item(models.Model):
    '''Model that define how the data will be stored for an item '''
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    quantity = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)])
    location = models.ForeignKey(
        'Location', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(
        'ItemStatus', limit_choices_to={'selectable': True}, null=True,
        blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        ''' String method to return the name of the item '''
        return str(self.name)

    def get_friendly_name(self):
        ''' String method to return the firendly name of the item '''
        return str(self.friendly_name)
