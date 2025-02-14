from django import forms
from .models import Feedback, ProductReview, Product, SecuritySettings, MarketplaceProduct, PrivacySettings, TwoFactorAuthentication, UserPrivacySettings, Storefront

# Feedback Form
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['product', 'service', 'rating', 'feedback_message']

# Product Review Form
class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['rating', 'comment']

# General Feedback Form
class GeneralFeedbackForm(forms.Form):
    feedback_text = forms.CharField(widget=forms.Textarea, required=True)

# Product Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']

# Marketplace Product Form
class MarketplaceProductForm(forms.ModelForm):
    class Meta:
        model = MarketplaceProduct
        fields = ['name', 'description', 'price', 'category', 'image', 'stock_quantity']

# Security Settings Form
class SecuritySettingsForm(forms.ModelForm):
    class Meta:
        model = SecuritySettings
        fields = ['two_factor_auth_enabled', 'email_notifications_enabled', 'profile_visibility', 'data_sharing_consent']

# Privacy Settings Form
class PrivacySettingsForm(forms.ModelForm):
    class Meta:
        model = UserPrivacySettings
        fields = ['share_email', 'share_phone_number', 'share_activity_status', 'share_profile', 'email_notifications', 'two_factor_auth']

# Two Factor Authentication Form
class TwoFactorAuthenticationForm(forms.ModelForm):
    class Meta:
        model = TwoFactorAuthentication
        fields = ['is_enabled']

# Storefront Form
class StorefrontForm(forms.ModelForm):
    class Meta:
        model = Storefront
        fields = ['name', 'description', 'channels']
