# serializers.py
from rest_framework import serializers
from .models import Website, Template, ContentBlock, BlogCategory, BlogPost, BlogCollaboration


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
