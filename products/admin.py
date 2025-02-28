

from django.utils.html import format_html
from django.contrib import admin
# Register your models here.
from .models import Category, Product, Img, Product_attribute, Attribute_value, Comment


admin.site.site_header = 'Falcom administration'
admin.site.site_title = 'Manage products'
admin.site.index_title = 'falcon shop admin'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}



class ProductImageInline(admin.TabularInline):
    model = Img


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','name','price','discount','stock')
    search_fields = ('name','description')
    list_filter = ('category',)
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)


@admin.register(Product_attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Attribute_value)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('product','attribute','value')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','rating','product')

