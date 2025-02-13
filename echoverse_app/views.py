from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .services import generate_ai_design, generate_ai_content, generate_seo_meta
from .models import BlogPost, Collaboration

# AI Design Design
def ai_design(request, industry):
    design = generate_ai_design(industry)
    return JsonResponse({'design': design})

# Add Section
def add_section(request, page_id, section_name, content):
    page = Page.objects.get(id=page_id)
    section = Section.objects.create(name=section_name, content=content)
    page.sections.add(section)
    return JsonResponse({'message': 'Section added successfully'})

# Get Page Sections
def get_page_sections(request, page_id):
    page = Page.objects.get(id=page_id)
    sections = page.sections.all()
    section_data = [{'name': section.name, 'content': section.content} for section in sections]
    return JsonResponse({'sections': section_data})

# AI Content
def ai_content(request, title):
    content = generate_ai_content(title)
    return JsonResponse({'title': title, 'content': content})

# Add Collaborator
def add_collaborator(request, post_id, user_id, role):
    post = get_object_or_404(BlogPost, id=post_id)
    user = get_object_or_404(User, id=user_id)
    Collaboration.objects.create(post=post, user=user, role=role)
    return JsonResponse({'message': f'Collaborator {user.username} added with role {role}'})

# SEO Meta
def seo_meta(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    seo_data = generate_seo_meta(post)
    return JsonResponse(seo_data)
