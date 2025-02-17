from django.db import models
from django.contrib.auth.models import User

# Website Models
class Website(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    theme = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Template Models
class Template(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    preview_image = models.ImageField(upload_to='templates/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Content Block Models
class ContentBlock(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    block_type = models.CharField(max_length=100)  # e.g., text, image, video
    content = models.TextField()
    position = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.block_type} Block for {self.website.name}"

# Blog Category Models
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# Blog Post Models
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=[('draft', 'Draft'), ('published', 'Published')])
    seo_title = models.CharField(max_length=255, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    seo_keywords = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

# Blog Collaboratopn Models
class BlogCollaboration(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('editor', 'Editor'), ('reviewer', 'Reviewer')])

    def __str__(self):
        return f"{self.user.username} - {self.role} for {self.post.title}"
