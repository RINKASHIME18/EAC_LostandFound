from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    # Options para sa Status at Category
    STATUS_CHOICES = [('Lost', 'Lost'), ('Found', 'Found')]
    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Documents', 'Documents'),
        ('Personal Effects', 'Personal Effects'),
        ('Others', 'Others'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    location = models.CharField(max_length=200) 
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='items/', null=True, blank=True) 

    # --- MGA BAGONG FIELDS (Dito ang fix sa error mo) ---
    date_lost = models.DateField(null=True, blank=True)
    time_lost = models.TimeField(null=True, blank=True)
    
    # Track who reported the item
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.status}: {self.title}"

class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items/')

    def __str__(self):
        return f"Image for {self.item.title}"
    