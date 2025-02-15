import openai
import stripe
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .services import generate_ai_design, generate_ai_content, generate_seo_meta, generate_product_description, generate_product_price, process_payment, send_email_campaign, send_security_email, generate_ad_content, chatbot
from .models import BlogPost, Collaboration, Product, SalesFunnel, SocialMediaPost, HomePage, UserDashboard, Contact, TermsAndPolicies, Footer, UserSecuritySettings, PrivacyPreferences, Feedback, ProductReview, ProductListing, SecuritySettings, MarketplaceProduct, MarketplaceTransaction, PrivacySettings, TwoFactorAuthentication, UserPrivacySettings, AIGeneratedContent, Storefront, AIProductDescription, Inventory, Order, Payment, AbandonedCart, Customer, EmailCampaign, AdCampaign
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm, ProductReviewForm, ProductForm. SecuritySettingsForm, PrivacySettingsForm, MarketplaceProductForm, StorefrontForm, InventoryForm
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.conf import settings
from .utils import generate_email_content, generate_ad_copy, generate_funnel_recommendations


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

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
def create_sales_funnel(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        stages = request.POST.get('stages', '[]')  # Default to empty list if not provided
        conversion_rate = request.POST.get('conversion_rate', None)

        try:
            stages = json.loads(stages)  # Convert JSON string to Python list
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format for stages'}, status=400)

        funnel = SalesFunnel.objects.create(
            name=name,
            description=description,
            stages=stages,
            conversion_rate=conversion_rate if conversion_rate else None  # Handle optional field
        )

        return redirect('sales_funnel_detail', funnel_id=funnel.id)

    return render(request, 'create_sales_funnel.html')

# Sales Funnel Detail
def sales_funnel_detail(request, funnel_id):
    funnel = get_object_or_404(SalesFunnel, id=funnel_id)

    # Ensure stages is a list (since it's stored as JSON)
    funnel_stages = funnel.stages if isinstance(funnel.stages, list) else []

    # Example: Generate recommendations based on the first stage
    user_behavior = "User has shown interest in product category X"
    recommendations = generate_funnel_recommendations(user_behavior, funnel_stages[0] if funnel_stages else "")

    return render(request, 'sales_funnel_detail.html', {
        'funnel': funnel,
        'recommendations': recommendations
    })

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
    user = request.user

    # Get user dashboard
    dashboard = UserDashboard.objects.get(user=user)

    # Get user marketplace products
    products = MarketplaceProduct.objects.filter(created_by=user)

    # Get user's privacy settings
    privacy_settings = UserPrivacySettings.objects.get(user=user)

    context = {
        'dashboard': dashboard,
        'products': products,
        'privacy_settings': privacy_settings,
    }
    return render(request, 'user_dashboard.html', context)

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
    terms = TermsAndPolicies.objects.filter(is_active=True)
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
            return redirect('feedback_thank_you')
    else:
        form = FeedbackForm()

    return render(request, 'submit_feedback.html', {'form': form})

# Submit Product Review
def submit_product_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user
            review.product = product
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductReviewForm()

    return render(request, 'submit_product_review.html', {'form': form, 'product': product})

# Submit General Feedback
def submit_general_feedback(request):
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback_text')
        if feedback_text:
            feedback = GeneralFeedback(user=request.user, feedback_text=feedback_text)
            feedback.save()
            return redirect('feedback_success')
    return render(request, 'submit_feedback.html')

# Product Details
def product_detail(request, product_id):
    # Try to get the product from both Product and MarketplaceProduct models
    try:
        product = get_object_or_404(Product, id=product_id)
        reviews = ProductReview.objects.filter(product=product)
        return render(request, 'product_detail.html', {'product': product, 'reviews': reviews})
    except Product.DoesNotExist:
        product = get_object_or_404(MarketplaceProduct, id=product_id, is_active=True)
        return render(request, 'product_detail.html', {'product': product})

# Create Product
@login_required
def create_product(request):
    if request.method == 'POST':
        form = MarketplaceProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = MarketplaceProductForm()
    return render(request, 'create_product.html', {'form': form})

# MarketPlace
def marketplace(request):
    products = Product.objects.filter(productlisting__active=True)  # Filter active listings only
    marketplace_products = MarketplaceProduct.objects.filter(is_active=True)

    template = 'marketplace_home.html' if 'home' in request.path else 'marketplace.html'

    return render(request, 'marketplace.html', {'products': products, 'marketplace_products': marketplace_products})

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

# Buy Product
@login_required
def buy_product(request, product_id):
    product = get_object_or_404(MarketplaceProduct, id=product_id, is_active=True)

    if product.stock > 0:
        transaction = MarketplaceTransaction.objects.create(
            buyer=request.user,
            product=product,
            quantity=1,
            total_price=product.price,
            status='pending'
        )
        product.stock -= 1
        product.save()
        return render(request, 'purchase_success.html', {'transaction': transaction})
    else:
        return render(request, 'purchase_failed.html', {'product': product})

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

# Privacy Settings
@login_required
def update_privacy_settings(request):
    try:
        privacy_settings = PrivacySettings.objects.get(user=request.user)
    except PrivacySettings.DoesNotExist:
        privacy_settings = PrivacySettings(user=request.user)

    if request.method == 'POST':
        form = PrivacySettingsForm(request.POST, instance=privacy_settings)
        if form.is_valid():
            form.save()
            return redirect('privacy_settings')
    else:
        form = PrivacySettingsForm(instance=privacy_settings)

    return render(request, 'privacy_settings.html', {'form': form})

# Two Factor Authentication
@login_required
def enable_two_factor_authentication(request):
    try:
        two_fa = TwoFactorAuthentication.objects.get(user=request.user)
    except TwoFactorAuthentication.DoesNotExist:
        two_fa = TwoFactorAuthentication(user=request.user)

    if request.method == 'POST':
        if not two_fa.is_enabled:
            two_fa.is_enabled = True
            two_fa.save()
            # Implement the logic for generating a secret key for 2FA here
        return redirect('two_factor_settings')

    return render(request, 'two_factor_settings.html', {'two_fa': two_fa})

# Privacy Settings
@login_required
def privacy_settings(request):
    privacy_settings, created = UserPrivacySettings.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PrivacySettingsForm(request.POST, instance=privacy_settings)
        if form.is_valid():
            form.save()
            return redirect('privacy_settings')
    else:
        form = PrivacySettingsForm(instance=privacy_settings)

    return render(request, 'privacy_settings.html', {'form': form})

# Generate AI Content
@login_required
def generate_ai_content(request):
    if request.method == 'POST':
        content_type = request.POST.get('content_type', 'Blog Post')
        prompt = request.POST.get('prompt', '')

        # Call the AI service to generate content
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # Example engine (change if needed)
                prompt=prompt,
                max_tokens=500
            )
            ai_content = response.choices[0].text.strip()

            # Store the generated content in the database
            new_content = AIGeneratedContent.objects.create(
                title=f"{content_type} for {prompt[:30]}...",
                content=ai_content,
                content_type=content_type
            )

            return render(request, 'generated_content.html', {'content': new_content})
        except Exception as e:
            return render(request, 'generate_ai_content.html', {'error': str(e)})

    return render(request, 'generate_ai_content.html')

# Create Storefront
@login_required
def create_storefront(request):
    if request.method == 'POST':
        form = StorefrontForm(request.POST)
        if form.is_valid():
            storefront = form.save(commit=False)
            storefront.owner = request.user
            storefront.save()
            return redirect('view_storefront', storefront_id=storefront.id)
    else:
        form = StorefrontForm()

    return render(request, 'create_storefront.html', {'form': form})

# View Storefront
@login_required
def view_storefront(request, storefront_id):
    storefront = Storefront.objects.get(id=storefront_id, owner=request.user)
    products = MarketplaceProduct.objects.filter(storefront=storefront)

    return render(request, 'view_storefront.html', {'storefront': storefront, 'products': products})

# Generate AI Product Description
@login_required
def generate_ai_product_description(request, product_id):
    product = MarketplaceProduct.objects.get(id=product_id, created_by=request.user)

    if request.method == 'POST':
        # Call AI to generate product description and pricing suggestion
        prompt = f"Generate a detailed description for a product named {product.name}."
        try:
            # AI description generation
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=300
            )
            description = response.choices[0].text.strip()

            # AI price suggestion based on product type
            price_response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Suggest a price for a product named {product.name}.",
                max_tokens=50
            )
            price_suggestion = float(price_response.choices[0].text.strip().replace('$', '').replace(',', ''))

            # Save the generated data
            ai_description = AIProductDescription.objects.create(
                product=product,
                description=description,
                price_suggestion=price_suggestion
            )

            return render(request, 'generated_product_description.html', {'product': product, 'ai_description': ai_description})
        except Exception as e:
            return render(request, 'generate_ai_product_description.html', {'error': str(e)})

    return render(request, 'generate_ai_product_description.html', {'product': product})

# Manage Inventory
@login_required
def manage_inventory(request):
    products = MarketplaceProduct.objects.filter(created_by=request.user)
    inventories = Inventory.objects.filter(product__in=products)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        inventory, created = Inventory.objects.get_or_create(product_id=product_id)
        inventory.quantity = quantity
        inventory.save()
        return redirect('manage_inventory')

    return render(request, 'manage_inventory.html', {'inventories': inventories, 'products': products})

# Manage Orders
@login_required
def manage_orders(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'manage_orders.html', {'orders': orders})

# Checkout
@login_required
def checkout(request, order_id):
    order = Order.objects.get(id=order_id, customer=request.user)

    if request.method == 'POST':
        try:
            # Create a Stripe Payment Intent
            intent = stripe.PaymentIntent.create(
                amount=int(order.total_price * 100),  # Amount in cents
                currency='usd',
                metadata={'order_id': order.id}
            )

            payment = Payment.objects.create(
                order=order,
                payment_method='stripe',
                amount=order.total_price,
                payment_id=intent['id'],
                payment_status='pending'
            )

            # Pass the client secret to the frontend to complete the payment
            return render(request, 'payment_page.html', {
                'client_secret': intent['client_secret'],
                'order': order
            })
        except stripe.error.StripeError as e:
            return render(request, 'checkout_error.html', {'error': str(e)})

    return render(request, 'checkout.html', {'order': order})

# Payment Success
@login_required
def payment_success(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    payment.payment_status = 'completed'
    payment.save()

    order = payment.order
    order.status = 'shipped'  # Update order status to shipped after successful payment
    order.save()

    return render(request, 'payment_success.html', {'payment': payment})

# Payment Failure
@login_required
def payment_failure(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    payment.payment_status = 'failed'
    payment.save()

    return render(request, 'payment_failure.html', {'payment': payment})

# Track Abandoned Cart
def track_abandoned_cart(request, product_id):
    if request.user.is_authenticated:
        abandoned_cart, created = AbandonedCart.objects.get_or_create(
            user=request.user, product_id=product_id
        )
        abandoned_cart.updated_at = timezone.now()
        abandoned_cart.save()

    return redirect('cart_view')  # Redirect to the cart view page

# Check Abandoned Cart
def check_abandoned_carts():
    # Find carts abandoned for more than 24 hours
    cutoff_time = timezone.now() - timedelta(hours=24)
    abandoned_carts = AbandonedCart.objects.filter(abandoned_at__lte=cutoff_time)

    for cart in abandoned_carts:
        send_abandoned_cart_email(cart.user, cart)
        cart.delete()

# Send Anandoned Cart Email
def send_abandoned_cart_email(user, cart):
    subject = "You left something behind!"
    message = f"Hello {user.username},\n\nIt looks like you left {cart.product.name} in your cart. Complete your purchase now!"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

# Cart View
@login_required
def cart_view(request):
    carts = AbandonedCart.objects.filter(user=request.user)
    return render(request, 'cart_view.html', {'carts': carts})

# Send Email Campaign
def send_email_campaign(request, campaign_id):
    campaign = EmailCampaign.objects.get(id=campaign_id)

    # Fetch all customers to send the email
    customers = Customer.objects.all()

    for customer in customers:
        # Generate personalized email content using AI
        email_content = generate_email_content(customer.name, customer.purchase_history.all())

        # Send the email
        send_mail(
            subject=campaign.subject,
            message=email_content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[customer.email],
        )

        # Update the campaign sent time
        campaign.sent_at = timezone.now()
        campaign.save()

    return redirect('campaign_sent', campaign_id=campaign.id)

# Campaign Sent
def campaign_sent(request, campaign_id):
    campaign = EmailCampaign.objects.get(id=campaign_id)
    return render(request, 'campaign_sent.html', {'campaign': campaign})

# Create Ad Campaign
def create_ad_campaign(request, product_id):
    product = MarketplaceProduct.objects.get(id=product_id)

    # Generate ad copy using AI
    ad_copy = generate_ad_copy(product.name, product.description, product.category)

    # Create the ad campaign and save it
    ad_campaign = AdCampaign.objects.create(
        name=f"Ad Campaign for {product.name}",
        product=product,
        ad_copy=ad_copy,
        status='Draft'
    )

    return redirect('ad_campaign_detail', ad_campaign_id=ad_campaign.id)

# Ad Campaign Detail
def ad_campaign_detail(request, ad_campaign_id):
    ad_campaign = AdCampaign.objects.get(id=ad_campaign_id)
    return render(request, 'ad_campaign_detail.html', {'ad_campaign': ad_campaign})
