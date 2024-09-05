from django.db import models
from django.conf import settings

class Category(models.TextChoices):
    ELECTRONICS = 'Electronics'
    FURNITURE = 'Furniture'
    CLOTHING = 'Clothing'
    BOOKS = 'Books'
    FOOD = 'Food'
    FOOD_ITEMS = 'Food_Items'
    HEALTH = 'Health'
    OTHER = 'Other'

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=Category.choices)
    images = models.ImageField(upload_to='listing_images/', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.title


