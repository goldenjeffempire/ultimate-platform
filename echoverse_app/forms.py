from django import forms
from .models import Feedback, ProductReview, Product, SecuritySettings, MarketplaceProduct

# Feedback Form
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['product', 'service', 'rating', 'feedback_message']

# Product Review Form
class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['rating', 'review_text']

# Product Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']

# Marketplace Product Form
class MarketplaceProductForm(forms.ModelForm):
    class Meta:
        model = MarketplaceProduct
        fields = ['name', 'description', 'price', 'stock', 'image']

# Security Settings Form
class SecuritySettingsForm(forms.ModelForm):
    class Meta:
        model = SecuritySettings
        fields = ['two_factor_auth_enabled', 'email_notifications_enabled', 'profile_visibility', 'data_sharing_consent']
