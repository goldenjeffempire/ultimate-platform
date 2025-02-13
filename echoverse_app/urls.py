from django.urls import path
from . import views

urlpatterns = [
    path('ai-design/<str:industry>/', views.ai_design, name='ai_design'),
    path('add-section/<int:page_id>/<str:section_name>/<str:content>/', views.add_section, name='add_section'),
    path('get-page-sections/<int:page_id>/', views.get_page_sections, name='get_page_sections'),
    path('ai-content/<str:title>/', views.ai_content, name='ai_content'),
    path('add-collaborator/<int:post_id>/<int:user_id>/<str:role>/', views.add_collaborator, name='add_collaborator'),
    path('seo-meta/<int:post_id>/', views.seo_meta, name='seo_meta'),
    path('generate-product-info/<int:product_id>/', views.generate_product_info, name='generate_product_info'),
    path('update-inventory/<int:product_id>/<int:quantity>/', views.update_inventory, name='update_inventory'),
    path('check-inventory/<int:product_id>/', views.check_inventory, name='check_inventory'),
]
