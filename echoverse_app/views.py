from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .services import generate_ai_design, generate_ai_content, generate_seo_meta, generate_product_description, generate_product_price, process_payment
from .models import BlogPost, Collaboration, Product

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
