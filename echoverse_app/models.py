from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import now

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

# Category
class Category(models.Model):
    CATEGORY_TYPE_CHOICES = [
        ('product', 'Product Category'),
        ('general', 'General Category'),
    ]

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    category_type = models.CharField(max_length=10, choices=CATEGORY_TYPE_CHOICES, default='general')

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

# Marketplace Product
class MarketplaceProduct(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='marketplace_products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='marketplace_products/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    marketplace_listing = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} by {self.seller.username}"

class EmailCampaign(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    scheduled_for = models.DateTimeField()
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class SalesFunnel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description provided")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FunnelStage(models.Model):
    funnel = models.ForeignKey(SalesFunnel, related_name="stages", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    conversion_rate = models.FloatField(default=0.0)  # Percentage of users moving to next stage

    def __str__(self):
        return f"{self.name} (Funnel: {self.funnel.name})"

class SocialMediaPost(models.Model):
    PLATFORM_CHOICES = [
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter'),
        ('LinkedIn', 'LinkedIn'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES, default='Facebook')
    scheduled_time = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)  # Unified field name
    created_at = models.DateTimeField(auto_now_add=True)  # Track creation time
    updated_at = models.DateTimeField(auto_now=True)  # Track last modification

    def __str__(self):
        return f"{self.platform} Post by {self.user.username if self.user else 'Unknown'}"

class HomePage(models.Model):
    title = models.CharField(max_length=255)
    intro_text = models.TextField()
    featured_products = models.ManyToManyField(MarketplaceProduct)
    banner_image = models.ImageField(upload_to='home/', null=True, blank=True)

    def __str__(self):
        return self.title

class UserDashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Dashboard"

class ContactMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.name}"


class TermsAndPolicies(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Footer(models.Model):
    content = models.TextField()

    def __str__(self):
        return "Footer Content"

# User Feedback
class UserFeedback(models.Model):
    FEEDBACK_TYPE_CHOICES = [
        ('product', 'Product Review'),
        ('service', 'Service Feedback'),
        ('general', 'General Feedback'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback')
    feedback_type = models.CharField(max_length=10, choices=FEEDBACK_TYPE_CHOICES)

    # MarketplaceProduct-related Feedback
    product = models.ForeignKey(
        MarketplaceProduct, on_delete=models.CASCADE, null=True, blank=True, related_name='feedback'
    )

    # Service-related feedback
    service_name = models.CharField(max_length=255, null=True, blank=True)

    # Shared fields
    message = models.TextField()  # Feedback text or review comment
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=True)  # Optional rating
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.feedback_type == 'product' and self.product:
            return f"Product Review: {self.user.username} on {self.product.name}"
        elif self.feedback_type == 'service' and self.service_name:
            return f"Service Feedback: {self.user.username} on {self.service_name}"
        return f"General Feedback by {self.user.username}"

# Marketplace Order
class MarketplaceOrder(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey('MarketplaceProduct', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name} by {self.buyer.username} (Status: {self.status})"

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    purchase_history = models.ManyToManyField(MarketplaceProduct, blank=True)
    last_contacted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class TwoFactorAuthentication(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=False)
    secret_key = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"2FA for {self.user.username}"

class AIGeneratedContent(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)
    content_type = models.CharField(max_length=50)  # e.g., 'Blog Post', 'Product Description'

    def __str__(self):
        return self.title

class Storefront(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='storefronts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Define supported sales channels (e.g., website, mobile app, social media)
    CHANNEL_CHOICES = [
        ('website', 'Website'),
        ('mobile', 'Mobile'),
        ('social_media', 'Social Media'),
    ]
    channels = models.CharField(max_length=50, choices=CHANNEL_CHOICES)

    def __str__(self):
        return f"Storefront: {self.name} ({self.channels})"

class AIProductDescription(models.Model):
    product = models.ForeignKey(MarketplaceProduct, on_delete=models.CASCADE, related_name='ai_descriptions')
    description = models.TextField()
    price_suggestion = models.DecimalField(max_digits=10, decimal_places=2)
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Description for {self.product.name}"

class Inventory(models.Model):
    product = models.ForeignKey(MarketplaceProduct, on_delete=models.CASCADE, related_name='inventory')
    quantity = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inventory for {self.product.name} - {self.quantity} in stock"

class Payment(models.Model):
    order = models.ForeignKey(MarketplaceOrder, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_status_choices = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    payment_status = models.CharField(max_length=10, choices=payment_status_choices, default='pending')
    payment_id = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order #{self.order.id} - Status: {self.payment_status}"

class AbandonedCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(MarketplaceProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    abandoned_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Cart for {self.user.username} - {self.product.name}"

class AdCampaign(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(MarketplaceProduct, on_delete=models.CASCADE)
    ad_copy = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Draft', 'Draft'), ('Active', 'Active'), ('Completed', 'Completed')], default='Draft')

    def __str__(self):
        return f"Ad Campaign for {self.product.name} - {self.status}"

class ChatSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Ended', 'Ended')], default='Active')

    def __str__(self):
        return f"Chat with {self.user.username} - {self.status}"

class ChatMessage(models.Model):
    chat_session = models.ForeignKey(ChatSession, related_name='messages', on_delete=models.CASCADE)
    sender = models.CharField(max_length=10, choices=[('User', 'User'), ('Bot', 'Bot')], default='User')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.chat_session.user.username} - {self.sender}"

class Ad(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    target_audience = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Draft')

    def __str__(self):
        return f"Ad: {self.title}"

class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} - {self.rating} Stars"

# User Security Privacy Settings
class UserSecurityPrivacySettings(models.Model):
    PROFILE_VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
        ('friends_only', 'Friends Only'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='security_privacy_settings')

    # Security Settings
    two_factor_enabled = models.BooleanField(default=False)
    email_notifications_enabled = models.BooleanField(default=True)
    password_changed_at = models.DateTimeField(auto_now=True)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)

    # Privacy Preferences
    share_profile_info = models.BooleanField(default=True)
    share_activity_with_friends = models.BooleanField(default=True)
    data_sharing_consent = models.BooleanField(default=False)

    # Privacy Settings
    share_email = models.BooleanField(default=True)
    share_phone_number = models.BooleanField(default=True)
    share_activity_status = models.BooleanField(default=True)

    # General Privacy Settings
    share_profile = models.BooleanField(default=True)
    profile_visibility = models.CharField(
        max_length=20,
        choices=PROFILE_VISIBILITY_CHOICES,
        default='public'
    )

    def __str__(self):
        return f"Security & Privacy settings for {self.user.username}"
