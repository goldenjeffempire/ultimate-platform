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
router.register(r'scholarships', views.ScholarshipViewSet)
router.register(r'sponsorships', views.SponsorshipViewSet)
router.register(r'student-performance', views.StudentPerformanceViewSet)
router.register(r'crm-contacts', views.CRMContactViewSet)
router.register(r'email-campaigns', views.EmailCampaignViewSet)
router.register(r'ad-campaigns', views.AdCampaignViewSet)
router.register(r'sales-funnels', views.SalesFunnelViewSet)
router.register(r'chatbot-interactions', views.ChatbotInteractionViewSet)
router.register(r'alumni', views.AlumniViewSet)
router.register(r'job-postings', views.JobPostingViewSet)
router.register(r'live-events', views.LiveEventViewSet)
router.register(r'mentorships', views.MentorshipViewSet)
router.register(r'user-roles', views.UserRoleViewSet)
router.register(r'activity-logs', views.ActivityLogViewSet)
router.register(r'leaderboards', views.LeaderboardViewSet)
router.register(r'badges', views.BadgeViewSet)
router.register(r'achievements', views.AchievementViewSet)
router.register(r'group-projects', views.GroupProjectViewSet)
router.register(r'portfolios', views.PortfolioViewSet)
router.register(r'knowledge-base', views.KnowledgeBaseArticleViewSet)
router.register(r'live-chat', views.LiveChatSessionViewSet)
router.register(r'tickets', views.TicketViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/ai/generate-content/', views.AIContentGenerationView.as_view(), name='generate-content'),  # Add the AI content generation endpoint
    path('api/register/', views.RegisterUserView.as_view(), name='register-user'),
    path('api/update-progress/', views.UpdateProgressView.as_view(), name='update-progress'),
    path('api/update-module-progress/', views.UpdateModuleProgressView.as_view(), name='update-module-progress'),
    path('api/update-student-performance/', views.UpdateStudentPerformanceView.as_view(), name='update-student-performance'),
]
