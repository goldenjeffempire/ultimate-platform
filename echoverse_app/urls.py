from django.urls import path
from . import views

urlpatterns = [
    path('ai-design/<str:industry>/', views.ai_design, name='ai_design'),
    path('add-section/<int:page_id>/<str:section_name>/<str:content>/', views.add_section, name='add_section'),
    path('get-page-sections/<int:page_id>/', views.get_page_sections, name='get_page_sections'),
]
