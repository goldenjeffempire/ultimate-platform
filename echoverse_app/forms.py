from django import forms
from .models import Feedback, ProductReview, Product, SecuritySettings, MarketplaceProduct, PrivacySettings, TwoFactorAuthentication

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

# Privacy Settings Form
class PrivacySettingsForm(forms.ModelForm):
    class Meta:
        model = PrivacySettings
        fields = ['share_email', 'share_phone_number', 'share_activity_status']

# Two Factor Authentication Form
class TwoFactorAuthenticationForm(forms.ModelForm):
    class Meta:
        model = TwoFactorAuthentication
        fields = ['is_enabled']
