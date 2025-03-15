from django.contrib import admin
from django.utils.html import format_html
from .models import CarouselImage, Product, ProductImage, WhyChooseUs, Testimonial

# ✅ Fix: Removed duplicate imports and registrations

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag', 'caption', 'created_at']
    search_fields = ['caption']
    list_filter = ['created_at']

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius: 5px;" />', obj.image.url)
        return "No Image"

    image_tag.short_description = "Image"

class ProductImageInline(admin.TabularInline):  
    model = ProductImage
    extra = 1  # Allows adding multiple images easily

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(ProductImage)
admin.site.register(WhyChooseUs)
admin.site.register(Testimonial)
