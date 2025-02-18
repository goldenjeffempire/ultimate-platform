# serializers.py
from rest_framework import serializers
from .models import Website, Template, ContentBlock, BlogCategory, BlogPost, BlogCollaboration, ProductCategory, Product, Order, Cart, ProductReview, UserProfile, Application, ProgressTrackerm, LearningModule, UserModuleProgress, Quiz, Question, UserQuizAnswer, Scholarship, Sponsorship, StudentPerformance, CRMContact, EmailCampaign, AdCampaign, SalesFunnel, ChatbotInteraction, Alumni, JobPosting, LiveEvent, Mentorship, UserRole, ActivityLog, KnowledgeBaseArticle, LiveChatSession, Ticket, StudentInsight, WebsiteAnalytics, ScholarshipImpactReport


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

# CRM Contact
class CRMContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMContact
        fields = ['id', 'user', 'first_name', 'last_name', 'email', 'phone', 'created_at']

# Email Campaign
class EmailCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCampaign
        fields = ['id', 'title', 'subject', 'content', 'sent_at']

# Ad Campaign
class AdCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdCampaign
        fields = ['id', 'title', 'platform', 'budget', 'start_date', 'end_date', 'created_at']

# Sales Funnel
class SalesFunnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesFunnel
        fields = ['id', 'name', 'description', 'created_at']

# Chatbot Interaction
class ChatbotInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatbotInteraction
        fields = ['id', 'user', 'message', 'response', 'interacted_at']

# Alumni
class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = ['id', 'user', 'graduation_year', 'degree', 'current_job', 'bio']

# Job Posting
class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ['id', 'title', 'description', 'company', 'location', 'posted_at']

# Live Event
class LiveEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveEvent
        fields = ['id', 'title', 'description', 'event_date', 'created_at']

# Mentorship
class MentorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = ['id', 'mentor', 'mentee', 'start_date', 'end_date', 'goals']

# User Role
class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id', 'name', 'permissions']

# Activty Log
class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = ['id', 'user', 'action', 'timestamp']

# Knowledge Base Article
class KnowledgeBaseArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeBaseArticle
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']

# Live Chat Session
class LiveChatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveChatSession
        fields = ['id', 'user', 'started_at', 'ended_at', 'is_active']

# Ticket
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'user', 'issue_description', 'status', 'created_at', 'updated_at']

# Student Insight
class StudentInsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInsight
        fields = ['id', 'student', 'courses_completed', 'quiz_scores', 'last_activity']

# Website Analytics
class WebsiteAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteAnalytics
        fields = ['id', 'page_visits', 'unique_visitors', 'session_duration_avg', 'bounce_rate']

# Scholarship Impact Report
class ScholarshipImpactReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipImpactReport
        fields = ['id', 'scholarship_name', 'students_affected', 'total_funding', 'success_rate']
