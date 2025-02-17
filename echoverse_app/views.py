# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Website, Template, ContentBlock, BlogCategory, BlogPost, BlogCollaboration, ProductCategory, Product, Order, Cart, ProductReview, UserProfile, Application, ProgressTracker, LearningModule, UserModuleProgress, Quiz, Question, UserQuizAnswer
from .serializers import WebsiteSerializer, TemplateSerializer, ContentBlockSerializer, BlogCategorySerializer, BlogPostSerializer, BlogCollaborationSerializer, ProductCategorySerializer, ProductSerializer, OrderSerializer, CartSerializer, ProductReviewSerializer, UserProfileSerializer, ApplicationSerializer, ProgressTrackerSerializer, LearningModuleSerializer, UserModuleProgressSerializer, QuizSerializer, QuestionSerializer, UserQuizAnswerSerializer
from .ai_logic import ai_generate_blog_content, ai_generate_design, ai_generate_content

# Website View Set
class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer

# Template View Set
class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

# Content Block View Set
class ContentBlockViewSet(viewsets.ModelViewSet):
    queryset = ContentBlock.objects.all()
    serializer_class = ContentBlockSerializer

# Blog Category View Set
class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

# Blog Post View Set
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

# Blog Collaboration View Set
class BlogCollaborationViewSet(viewsets.ModelViewSet):
    queryset = BlogCollaboration.objects.all()
    serializer_class = BlogCollaborationSerializer

# AI Content  Generation (API View)
class AIContentGenerationView(APIView):
    def post(self, request):
        topic = request.data.get('topic')
        content = ai_generate_blog_content(topic)
        return Response(content, status=status.HTTP_200_OK)

# Product Category
class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

# Product
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Order View
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Cart View
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# Product Review
class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer

# User profile
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# Application
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

# Progress Tracker
class ProgressTrackerViewSet(viewsets.ModelViewSet):
    queryset = ProgressTracker.objects.all()
    serializer_class = ProgressTrackerSerializer

# Register User
class RegisterUserView(APIView):
    def post(self, request):
        # Custom user registration logic
        # For simplicity, assume that the user registration is done using Django's built-in user system
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({"detail": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        UserProfile.objects.create(user=user)

        return Response({"detail": "User registered successfully."}, status=status.HTTP_201_CREATED)

# Update Progress
class UpdateProgressView(APIView):
    def post(self, request):
        user = request.user  # Assuming user is authenticated
        progress_step = request.data.get('progress_step')
        completed = request.data.get('completed', False)

        progress, created = ProgressTracker.objects.get_or_create(
            user=user, progress_step=progress_step
        )
        progress.completed = completed
        progress.save()

        return Response({"detail": "Progress updated."}, status=status.HTTP_200_OK)

# Learning Module
class LearningModuleViewSet(viewsets.ModelViewSet):
    queryset = LearningModule.objects.all()
    serializer_class = LearningModuleSerializer

# User Module Progress
class UserModuleProgressViewSet(viewsets.ModelViewSet):
    queryset = UserModuleProgress.objects.all()
    serializer_class = UserModuleProgressSerializer

# Quiz
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

# Question
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# User Quiz Answer
class UserQuizAnswerViewSet(viewsets.ModelViewSet):
    queryset = UserQuizAnswer.objects.all()
    serializer_class = UserQuizAnswerSerializer

# Update Module Progress
class UpdateModuleProgressView(APIView):
    def post(self, request):
        user = request.user  # Assuming user is authenticated
        module_id = request.data.get('module_id')
        progress = request.data.get('progress')

        module = LearningModule.objects.get(id=module_id)
        user_progress, created = UserModuleProgress.objects.get_or_create(
            user=user, module=module
        )
        user_progress.progress = progress
        user_progress.save()

        return Response({"detail": "Module progress updated."}, status=status.HTTP_200_OK)
