from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import Category
from .models import Shop
from .models import Review
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display= ['title']

class ShopAdmin(admin.ModelAdmin):
    list_display= ['title', 'phone', 'created_at']

class ReviewAdmin(admin.ModelAdmin):
    list_display= ['title', 'username', 'created_at']

admin.site.register(Post, PostAdmin)

