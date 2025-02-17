# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'websites', views.WebsiteViewSet)
router.register(r'templates', views.TemplateViewSet)
router.register(r'content-blocks', views.ContentBlockViewSet)
router.register(r'blog-categories', views.BlogCategoryViewSet)
router.register(r'blog-posts', views.BlogPostViewSet)
router.register(r'blog-collaborations', views.BlogCollaborationViewSet)
router.register(r'product-categories', views.ProductCategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'product-reviews', views.ProductReviewViewSet)
router.register(r'user-profiles', views.UserProfileViewSet)
router.register(r'applications', views.ApplicationViewSet)
router.register(r'progress-tracker', views.ProgressTrackerViewSet)
router.register(r'learning-modules', views.LearningModuleViewSet)
router.register(r'user-module-progress', views.UserModuleProgressViewSet)
router.register(r'quizzes', views.QuizViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'user-quiz-answers', views.UserQuizAnswerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/ai/generate-content/', views.AIContentGenerationView.as_view(), name='generate-content'),  # Add the AI content generation endpoint
    path('api/register/', views.RegisterUserView.as_view(), name='register-user'),
    path('api/update-progress/', views.UpdateProgressView.as_view(), name='update-progress'),
    path('api/update-module-progress/', views.UpdateModuleProgressView.as_view(), name='update-module-progress'),
]
