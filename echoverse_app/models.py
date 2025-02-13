from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Website(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    template = models.ForeignKey('Template', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Template(models.Model):
    name = models.CharField(max_length=255)
    template_type = models.CharField(max_length=50)
    content = models.JSONField()

    def __str__(self):
        return self.name

class IndustryTemplate(models.Model):
    industry = models.CharField(max_length=255)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.industry} Template"

class Section(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.name

class Page(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    sections = models.ManyToManyField(Section)

    def __str__(self):
        return f"Page for {self.website.name}"

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Collaboration(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('editor', 'Editor'), ('viewer', 'Viewer')])

    def __str__(self):
        return f"{self.user.username} - {self.role} for {self.post.title}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')])
    shipping_address = models.TextField()

    def __str__(self):
        return f"Order #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Customer {self.user.username}"

class EmailCampaign(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class SalesFunnel(models.Model):
    name = models.CharField(max_length=255)
    steps = models.TextField()  # Comma-separated list of funnel steps
    conversion_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class SocialMediaPost(models.Model):
    content = models.TextField()
    scheduled_for = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"Post scheduled for {self.scheduled_for}"

class HomePage(models.Model):
    title = models.CharField(max_length=255)
    intro_text = models.TextField()
    featured_products = models.ManyToManyField(Product)
    banner_image = models.ImageField(upload_to='home/', null=True, blank=True)

    def __str__(self):
        return self.title

class UserDashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Dashboard"

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"

class TermsAndPolicies(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class Footer(models.Model):
    content = models.TextField()

    def __str__(self):
        return "Footer Content"
