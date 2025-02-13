import random

def generate_ai_design(industry):
    # This is a basic example. You can integrate with an AI design API here.
    designs = {
        'ecommerce': ['E-commerce Template A', 'E-commerce Template B'],
        'blog': ['Blog Template A', 'Blog Template B'],
        'personal': ['Personal Website Template A', 'Personal Website Template B'],
    }
    return random.choice(designs.get(industry, ['Default Template']))
