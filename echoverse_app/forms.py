from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import (
    MarketplaceOrder, MarketplaceProduct, SecuritySettings, UserPrivacySettings,
    Storefront, Inventory, SalesFunnel, FunnelStage, SocialMediaPost, ContactMessage, 
)

# Marketplace Order Form
class MarketplaceOrderForm(forms.ModelForm):
    class Meta:
        model = MarketplaceOrder
        fields = ['product', 'quantity', 'shipping_address']

# Marketplace Product Form
class MarketplaceProductForm(forms.ModelForm):
    class Meta:
        model = MarketplaceProduct
        fields = ['name', 'description', 'price', 'category', 'image', 'stock_quantity']

# Security Settings Form
class SecuritySettingsForm(forms.ModelForm):
    class Meta:
        model = SecuritySettings
        fields = ['two_factor_enabled', 'email_notifications_enabled', 'profile_visibility', 'data_sharing_consent']

# Privacy Settings Form
class PrivacySettingsForm(forms.ModelForm):
    class Meta:
        model = UserPrivacySettings
        fields = ['share_profile', 'email_notifications', 'two_factor_auth']

# Storefront Form
class StorefrontForm(forms.ModelForm):
    class Meta:
        model = Storefront
        fields = ['name', 'description', 'channels']

# Inventory Form
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['quantity']

# Sales Funnel Form
class SalesFunnelForm(forms.ModelForm):
    class Meta:
        model = SalesFunnel
        fields = ['name', 'description']

# Funnel Stage Form
class FunnelStageForm(forms.ModelForm):
    class Meta:
        model = FunnelStage
        fields = ['name', 'order', 'conversion_rate']

# Social Media Post Form
class SocialMediaPostForm(forms.ModelForm):
    class Meta:
        model = SocialMediaPost
        fields = ['content', 'platform', 'scheduled_time']

# Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

# Custom Password Change Form
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
