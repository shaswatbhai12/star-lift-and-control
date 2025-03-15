from django.shortcuts import render, get_object_or_404
from .models import CarouselImage, Product, Testimonial, ProductImage

# Home Page View
def home(request):
    carousel_images = CarouselImage.objects.all()
    products = Product.objects.all()
    testimonials = Testimonial.objects.all()  # Fetch testimonials
    
    return render(request, 'home/index.html', {
        'carousel_images': carousel_images,
        'products': products,
        'testimonials': testimonials
    })

# Product Detail View
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_images = ProductImage.objects.filter(product=product)  # Fetch all sub-products (images)

    return render(request, 'home/product_detail.html', {
        'product': product,
        'product_images': product_images,
    })

# Sub-Product Detail View
def sub_product_detail(request, image_id):
    sub_product = get_object_or_404(ProductImage, id=image_id)  # Get clicked sub-product
    product = sub_product.product  # Get parent product
    related_images = ProductImage.objects.filter(product=product)  # Fetch related images

    return render(request, 'home/sub_product_detail.html', {
        'sub_product': sub_product,
        'related_images': related_images,
    })
