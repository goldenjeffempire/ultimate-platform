from django.shortcuts import render
from django.http import JsonResponse
from .services import generate_ai_design

def ai_design(request, industry):
    design = generate_ai_design(industry)
    return JsonResponse({'design': design})

def add_section(request, page_id, section_name, content):
    page = Page.objects.get(id=page_id)
    section = Section.objects.create(name=section_name, content=content)
    page.sections.add(section)
    return JsonResponse({'message': 'Section added successfully'})

def get_page_sections(request, page_id):
    page = Page.objects.get(id=page_id)
    sections = page.sections.all()
    section_data = [{'name': section.name, 'content': section.content} for section in sections]
    return JsonResponse({'sections': section_data})
