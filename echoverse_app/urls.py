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


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/ai/generate-content/', AIContentGenerationView.as_view(), name='generate-content'),  # Add the AI content generation endpoint

]
