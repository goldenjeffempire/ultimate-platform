import openai
from django.conf import settings

# Set up OpenAI API
openai.api_key = settings.OPENAI_API_KEY

# Generate Email Content
def generate_email_content(customer_name, products):
    prompt = f"Generate a personalized email for {customer_name} about these products: {', '.join([product.name for product in products])}. The tone should be friendly and professional."

    response = openai.Completion.create(
        engine="text-davinci-003",  # or use the most suitable GPT model
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )

    return response.choices[0].text.strip()

# Generate Hard Copy
def generate_ad_copy(product_name, product_description, product_category):
    prompt = f"Create an engaging and creative advertisement for a product named {product_name}. It is a {product_category} and has the following features: {product_description}. The tone should be persuasive and attention-grabbing."

    response = openai.Completion.create(
        engine="text-davinci-003",  # or use the most suitable GPT model
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )

    return response.choices[0].text.strip()
