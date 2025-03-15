from django.db import models

# Carousel Images Model
class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    title = models.CharField(max_length=100, blank=True, null=True)  # Optional
    caption = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # Newest images first
        verbose_name = "Carousel Image"
        verbose_name_plural = "Carousel Images"

    def __str__(self):
        return self.title if self.title else (self.caption if self.caption else f"Image {self.id}")


# Product Model (Main Product Page)
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)  # Ensure this field exists
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name


# Sub-Product Images (Product Detail → Sub-Product Page)
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/")
    description = models.CharField(max_length=255, blank=True, null=True)  # Sub-product description

    def __str__(self):
        return f"Image for {self.product.name}"


# Why Choose Us Section Model
class WhyChooseUs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='why_choose_us/icons/', null=True, blank=True)

    def __str__(self):
        return self.title


# Testimonials Model
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)  # Optional profile image
    feedback = models.TextField()
    rating = models.IntegerField(default=5)  # Rating out of 5
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Projects Model (Linked to Products)
class Project(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='projects')
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return f"Project for {self.product.name}"
