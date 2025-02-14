from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .services import generate_ai_design, generate_ai_content, generate_seo_meta, generate_product_description, generate_product_price, process_payment, send_email_campaign, send_security_email, generate_ad_content, chatbot
from .models import BlogPost, Collaboration, Product, SalesFunnel, SocialMediaPost, HomePage, UserDashboard, Contact, TermsAndPolicies, Footer, UserSecuritySettings, PrivacyPreferences, Feedback, ProductReview, ProductListing, SecuritySettings
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm, ProductReviewForm, ProductForm. SecuritySettingsForm
from django_otp.plugins.otp_totp.models import TOTPDevice


# AI Design Design
def ai_design(request, industry):
    design = generate_ai_design(industry)
    return JsonResponse({'design': design})

# Add Section
def add_section(request, page_id, section_name, content):
    page = Page.objects.get(id=page_id)
    section = Section.objects.create(name=section_name, content=content)
    page.sections.add(section)
    return JsonResponse({'message': 'Section added successfully'})

# Get Page Sections
def get_page_sections(request, page_id):
    page = Page.objects.get(id=page_id)
    sections = page.sections.all()
    section_data = [{'name': section.name, 'content': section.content} for section in sections]
    return JsonResponse({'sections': section_data})

# AI Content
def ai_content(request, title):
    content = generate_ai_content(title)
    return JsonResponse({'title': title, 'content': content})

# Add Collaborator
def add_collaborator(request, post_id, user_id, role):
    post = get_object_or_404(BlogPost, id=post_id)
    user = get_object_or_404(User, id=user_id)
    Collaboration.objects.create(post=post, user=user, role=role)
    return JsonResponse({'message': f'Collaborator {user.username} added with role {role}'})

# SEO Meta
def seo_meta(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    seo_data = generate_seo_meta(post)
    return JsonResponse(seo_data)

# Generate Product Info
def generate_product_info(request, product_id):
    product = Product.objects.get(id=product_id)
    description = generate_product_description(product.name)
    price = generate_product_price(product.price)

    return JsonResponse({
        'product_name': product.name,
        'description': description,
        'price': price
    })

# Update Inventory
def update_inventory(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    product.stock += quantity
    product.save()
    return JsonResponse({'message': f'Inventory for {product.name} updated to {product.stock}'})

# Check Inventory
def check_inventory(request, product_id):
    product = Product.objects.get(id=product_id)
    return JsonResponse({'product_name': product.name, 'stock': product.stock})

# Process Order Payment
def process_order_payment(request, order_id):
    payment_info = {
        'amount': float(request.GET.get('amount'))  # Simulate getting payment data from request
    }
    if process_payment(order_id, payment_info):
        return JsonResponse({'message': 'Payment successful'})
    else:
        return JsonResponse({'message': 'Payment failed'}, status=400)

# Generate Ad Content
def generate_ad(request, product_name, target_audience):
    ad_content = generate_ad_content(product_name, target_audience)
    return JsonResponse({'ad_content': ad_content})

# Create Sales Funnel
def create_sales_funnel(request, name, steps, conversion_rate):
    funnel = SalesFunnel.objects.create(
        name=name,
        steps=steps,
        conversion_rate=conversion_rate
    )
    return JsonResponse({'message': f'Sales funnel {funnel.name} created successfully'})

# Schedule Post
def schedule_post(request, content, scheduled_for):
    scheduled_for = timezone.datetime.fromisoformat(scheduled_for)  # Convert string to datetime
    post = SocialMediaPost.objects.create(content=content, scheduled_for=scheduled_for)
    return JsonResponse({'message': f"Post scheduled for {scheduled_for}"})

# Chatbot
def chatbot(request, query):
    response = chatbot_response(query)
    return JsonResponse({'response': response})

# HomePage
def home(request):
    homepage = HomePage.objects.first()
    return render(request, 'home.html', {'homepage': homepage})

# User Dashboard
@login_required
def user_dashboard(request):
    dashboard = UserDashboard.objects.get(user=request.user)
    return render(request, 'dashboard.html', {'dashboard': dashboard})

# Contact
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return JsonResponse({'message': 'Your message has been sent successfully.'})

    return render(request, 'contact.html')

# Terms And Policies
def terms_and_policies(request):
    terms = TermsAndPolicies.objects.first()
    return render(request, 'terms_and_policies.html', {'terms': terms})

# Footer
def footer(request):
    footer_content = Footer.objects.first()
    return render(request, 'footer.html', {'footer': footer_content})

# Security Settings
@login_required
def security_settings(request):
    settings, created = UserSecuritySettings.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        settings.two_factor_enabled = request.POST.get('two_factor_enabled') == 'on'
        settings.email_notifications_enabled = request.POST.get('email_notifications_enabled') == 'on'
        settings.password_changed_at = timezone.now()
        settings.save()
        return redirect('security_settings')

    return render(request, 'security_settings.html', {'settings': settings})
y
# Privacy Preferences
@login_required
def privacy_preferences(request):
    preferences, created = PrivacyPreferences.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        preferences.share_profile_info = request.POST.get('share_profile_info') == 'on'
        preferences.share_activity_with_friends = request.POST.get('share_activity_with_friends') == 'on'
        preferences.data_usage_consent = request.POST.get('data_usage_consent') == 'on'
        preferences.save()
        return redirect('privacy_preferences')

    return render(request, 'privacy_preferences.html', {'preferences': preferences})

# Security Settings
@login_required
def security_settings(request):
    settings, created = UserSecuritySettings.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        settings.two_factor_enabled = request.POST.get('two_factor_enabled') == 'on'
        settings.email_notifications_enabled = request.POST.get('email_notifications_enabled') == 'on'
        settings.password_changed_at = timezone.now()
        settings.save()

        # Send an email notification if email notifications are enabled
        if settings.email_notifications_enabled:
            send_security_email(request.user)

        return redirect('security_settings')

    return render(request, 'security_settings.html', {'settings': settings})

# Submit Feedback
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()

    return render(request, 'submit_feedback.html', {'form': form})

# Submit Product Review
def submit_product_review(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product_detail', product_id=product.id)  # Assuming product_detail view exists
    else:
        form = ProductReviewForm()

    return render(request, 'submit_product_review.html', {'form': form, 'product': product})

# Product Details
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = ProductReview.objects.filter(product=product)
    return render(request, 'product_detail.html', {'product': product, 'reviews': reviews})

# MarketPlace
def marketplace(request):
    products = Product.objects.filter(productlisting__active=True)  # Filter active listings only
    return render(request, 'marketplace.html', {'products': products})

# List Product
@login_required
def list_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            ProductListing.objects.create(product=product)
            return redirect('marketplace')
    else:
        form = ProductForm()

    return render(request, 'list_product.html', {'form': form})

# Security Settings
@login_required
def security_settings(request):
    try:
        settings = SecuritySettings.objects.get(user=request.user)
    except SecuritySettings.DoesNotExist:
        settings = SecuritySettings(user=request.user)

    if request.method == 'POST':
        form = SecuritySettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            if settings.two_factor_auth_enabled:
                TOTPDevice.objects.create(user=request.user)
            return redirect('security_settings')
    else:
        form = SecuritySettingsForm(instance=settings)

    return render(request, 'security_settings.html', {'form': form})
