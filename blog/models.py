from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:category_detail', args=[self.pk])

class Shop(models.Model):
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:shop_detail', args=[self.pk])

class Review(models.Model):
    title = models.CharField(max_length=100)
    username = models.CharField(max_length=15)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

