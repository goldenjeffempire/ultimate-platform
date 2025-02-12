import random
from django.core.mail import send_mail
from .models import EmailCampaign

def generate_ai_design(industry):
    # This is a basic example. You can integrate with an AI design API here.
    designs = {
        'ecommerce': ['E-commerce Template A', 'E-commerce Template B'],
        'blog': ['Blog Template A', 'Blog Template B'],
        'personal': ['Personal Website Template A', 'Personal Website Template B'],
    }
    return random.choice(designs.get(industry, ['Default Template']))

def generate_ai_content(title):
    # Basic example; this can be connected to an actual AI service
    content_samples = [
        "This is a great article about {title}. It will cover various aspects of the topic and provide useful insights.",
        "The topic of {title} has become increasingly popular. This post will explore the key trends in this area.",
        "In this post, we will dive into the depths of {title} and share expert opinions and advice."
    ]
    content = random.choice(content_samples).format(title=title)
    return content

def generate_seo_meta(post):
    title = post.title
    description = post.content[:160]  # First 160 characters of content as description
    keywords = [word for word in post.content.split() if len(word) > 3]  # Extract keywords
    return {
        'title': title,
        'description': description,
        'keywords': ', '.join(keywords[:10])  # Limit to first 10 keywords
    }

def generate_product_description(product_name):
    # Basic AI-based description generator (to be replaced with actual AI integration)
    descriptions = [
        f"{product_name} is an exceptional product designed for quality and durability.",
        f"Introducing {product_name}, the best in class with features that redefine performance.",
        f"{product_name} provides unparalleled value and quality, perfect for your needs."
    ]
    return random.choice(descriptions)

def generate_product_price(base_price):
    # Simple AI-based pricing suggestion (this could be replaced with machine learning or market data)
    markup = random.uniform(1.1, 1.5)  # Random markup between 10% and 50%
    return round(base_price * markup, 2)

def process_payment(order_id, payment_info):
    # Placeholder function. Replace with actual payment gateway integration.
    order = Order.objects.get(id=order_id)
    if payment_info['amount'] == order.total_amount:
        order.status = 'paid'
        order.save()
        return True
    return False

def send_email_campaign(campaign_id):
    campaign = EmailCampaign.objects.get(id=campaign_id)
    customers = Customer.objects.all()
    for customer in customers:
        send_mail(
            campaign.subject,
            campaign.content,
            'from@example.com',  # Use the appropriate sender email
            [customer.email],
        )
    campaign.sent_at = timezone.now()
    campaign.save()
    return True

def send_security_email(user):
    send_mail(
        'Security Alert: Changes to Your Account',
        'Your security settings have been updated. Please review them.',
        'from@example.com',
        [user.email],
    )

def generate_ad_content(product_name, target_audience):
    # Placeholder function to simulate ad content generation.
    return f"Buy {product_name} now and get exclusive offers! Perfect for {target_audience}."

def chatbot_response(query):
    responses = {
        'hello': 'Hi! How can I help you today?',
        'product info': 'Please visit our product page for more details.',
        'order status': 'You can check your order status in your account dashboard.',
    }
    return responses.get(query.lower(), "I'm sorry, I didn't understand that.")
