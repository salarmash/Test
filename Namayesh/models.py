from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="image", blank=True, null=True)
    caption = models.TextField()
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ManyToManyField(Category, related_name="products")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date",)

    def __str__(self):
        return self.title
