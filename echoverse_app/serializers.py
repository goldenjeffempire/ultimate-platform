# serializers.py
from rest_framework import serializers
from .models import Website, Template, ContentBlock, BlogCategory, BlogPost, BlogCollaboration, ProductCategory, Product, Order, Cart, ProductReview, UserProfile, Application, ProgressTrackerm, LearningModule, UserModuleProgress, Quiz, Question, UserQuizAnswer, Scholarship, Sponsorship, StudentPerformance


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

# User Profile
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio', 'profile_picture']

# Application
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'user', 'application_status', 'submitted_at', 'last_updated_at']

# Progress Tracker
class ProgressTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressTracker
        fields = ['id', 'user', 'progress_step', 'completed', 'timestamp']

# Learning Module
class LearningModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningModule
        fields = ['id', 'title', 'description', 'created_at']

# User Module Progress
class UserModuleProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModuleProgress
        fields = ['id', 'user', 'module', 'progress']

# Quiz
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'module', 'created_at']

# Question
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'question_text', 'correct_answer']

# User Quiz Answer
class UserQuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuizAnswer
        fields = ['id', 'user', 'quiz', 'answer']

# Scholarship
class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = ['id', 'title', 'description', 'eligibility_criteria', 'created_at']

# Sponsorship
class SponsorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsorship
        fields = ['id', 'title', 'description', 'funding_amount', 'created_at']

# Student Performance
class StudentPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPerformance
        fields = ['id', 'student', 'grade', 'comments', 'tracked_at']
