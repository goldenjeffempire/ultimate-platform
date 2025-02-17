# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Website, Template, ContentBlock, BlogCategory, BlogPost, BlogCollaboration
from .serializers import WebsiteSerializer, TemplateSerializer, ContentBlockSerializer, BlogCategorySerializer, BlogPostSerializer, BlogCollaborationSerializer
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
