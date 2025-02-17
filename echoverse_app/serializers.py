# serializers.py
from rest_framework import serializers
from .models import Website, Template, ContentBlock, BlogCategory, BlogPost, BlogCollaboration, ProductCategory, Product, Order, Cart, ProductReview


# Website Serializer
class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ['id', 'user', 'name', 'domain', 'theme', 'created_at']

# Template Serializer
class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ['id', 'name', 'category', 'preview_image', 'created_at']

# Content Block Serializer
class ContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = ['id', 'website', 'block_type', 'content', 'position']

# Blog Category Serializer
class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'description']

# Blog Post Serializer
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'author', 'category', 'title', 'content', 'created_at', 'updated_at', 'status']

# Blog Collaboration Serializer
class BlogCollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCollaboration
        fields = ['id', 'post', 'user', 'role']

# Product Category
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'description']

# Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'seller', 'category', 'name', 'description', 'price', 'stock_quantity', 'image', 'created_at']

# Order
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'quantity', 'total_price', 'order_status', 'created_at']

# Cart
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'quantity']

# Product Review
class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ['id', 'product', 'user', 'rating', 'comment']
