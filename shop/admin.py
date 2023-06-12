from django.contrib import admin
from .models import User, Category, Sub_category, Product, Order, Contact_store

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'chat_id', 'phone', 'address']
    fields = ['username', 'first_name', 'last_name', 'chat_id', 'phone', 'address']
    search_fields = ['username', 'first_name', 'last_name', 'chat_id', 'phone', 'address']
    ordering = ['username', 'first_name', 'last_name', 'chat_id', 'phone', 'address']
    actions = ['make_published']
    actions = ['delete_queryset']
    list_display_links = ['username', 'first_name', 'last_name', 'chat_id', 'phone', 'address']

    def make_published(self, request, queryset):
        queryset.update(status=True)
    make_published.short_description = "Mark selected stories as published"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): 
    list_display = ['name', 'discription', 'image']
    fields = ['name', 'discription', 'image']
    search_fields = ['name', 'discription', 'image']
    ordering = ['name', 'discription', 'image']
    actions = ['make_published']
    list_display_links = ['name', 'discription', 'image']

    def make_published(self, request, queryset):
        queryset.update(status=True)
    make_published.short_description = "Mark selected stories as published"

@admin.register(Sub_category)
class Sub_categoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'discription', 'image', 'category']
    fields = ['name', 'discription', 'image', 'category']
    search_fields = ['name', 'discription', 'image', 'category']
    ordering = ['name', 'discription', 'image', 'category']
    actions = ['make_published']
    list_display_links = ['name', 'discription', 'image', 'category']

    def make_published(self, request, queryset):
        queryset.update(status=True)
    make_published.short_description = "Mark selected stories as published"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'discription', 'image', 'price', 'sub_category']
    fields = ['name', 'discription', 'image', 'price', 'sub_category']
    search_fields = ['name', 'discription', 'image', 'price', 'sub_category']
    ordering = ['name', 'discription', 'image', 'price', 'sub_category']
    actions = ['make_published']
    list_display_links = ['name', 'discription', 'image', 'price', 'sub_category']

    def make_published(self, request, queryset):
        queryset.update(status=True)
    make_published.short_description = "Mark selected stories as published"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'count', 'address', 'phone', 'status']
    fields = ['user', 'product', 'count', 'address', 'phone', 'status']
    search_fields = ['user', 'product', 'count', 'address', 'phone', 'status']
    ordering = ['user', 'product', 'count', 'address', 'phone', 'status']
    actions = ['make_published']
    list_display_links = ['user', 'product', 'count', 'address', 'phone', 'status']

    # delete order status true
    def delete_queryset(self, request, queryset):
        queryset.update(status=True)
    delete_queryset.short_description = "Mark selected stories as published"


    def make_published(self, request, queryset):
        queryset.update(status=True)
    make_published.short_description = "Mark selected stories as published"

@admin.register(Contact_store)
class Contact_storeAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'location', 'image', 'address']
    fields = ['name', 'phone', 'location', 'image', 'address']
    search_fields = ['name', 'phone', 'location', 'image', 'address']
    ordering = ['name', 'phone', 'location', 'image', 'address']
    actions = ['make_published']
    list_display_links = ['name', 'phone', 'location', 'image', 'address']
    

    def make_published(self, request, queryset):
        queryset.update(status=True)
    make_published.short_description = "Mark selected stories as published"

