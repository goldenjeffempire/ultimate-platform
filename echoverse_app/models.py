from django.db import models
from django.contrib.auth.models import User


class Website(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    template = models.ForeignKey('Template', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Template(models.Model):
    name = models.CharField(max_length=255)
    template_type = models.CharField(max_length=50)
    content = models.JSONField()

    def __str__(self):
        return self.name

class IndustryTemplate(models.Model):
    industry = models.CharField(max_length=255)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.industry} Template"

class Section(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.name

class Page(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    sections = models.ManyToManyField(Section)

    def __str__(self):
        return f"Page for {self.website.name}"

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Collaboration(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('editor', 'Editor'), ('viewer', 'Viewer')])

    def __str__(self):
        return f"{self.user.username} - {self.role} for {self.post.title}"
