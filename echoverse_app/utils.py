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

# Generate Funnel Recommendations
def generate_funnel_recommendations(user_behavior, funnel_stage):
    prompt = f"Given the user behavior: {user_behavior} and the current funnel stage: {funnel_stage}, suggest personalized recommendations or actions to move the user to the next stage of the sales funnel."

    response = openai.Completion.create(
        engine="text-davinci-003",  # or use the most suitable GPT model
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )

    return response.choices[0].text.strip()

# Generate ChatBot Response
def generate_chatbot_response(user_message, chat_history):
    prompt = f"The following is a conversation between a user and a helpful AI chatbot.\n{chat_history}\nUser: {user_message}\nChatbot:"

    response = openai.Completion.create(
        engine="text-davinci-003",  # or use the most suitable GPT model
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )

    return response.choices[0].text.strip()

# Generate Ad Content
def generate_ad_content(product_name, target_audience, ad_type):
    prompt = f"Generate an {ad_type} ad for a product called {product_name} targeting {target_audience}. Include a compelling title and description."

    response = openai.Completion.create(
        engine="text-davinci-003",  # or use the most suitable GPT model
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )

    return response.choices[0].text.strip()
