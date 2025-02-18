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

# Product Category Models
class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# Product Models
class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Order Models
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

# Cart Models
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Cart for {self.user.username}"

# Product Review Models
class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"

# User Profile Models
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

# Application Models
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    application_status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])
    submitted_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Application of {self.user.username}"

# Progress Tracker
class ProgressTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    progress_step = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Progress for {self.user.username} - {self.progress_step}"

# Learning Module Models
class LearningModule(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# User Module Progress
class UserModuleProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(LearningModule, on_delete=models.CASCADE)
    progress = models.DecimalField(max_digits=5, decimal_places=2)  # Percentage of completion

    def __str__(self):
        return f"{self.user.username} - {self.module.title} - {self.progress}%"

# Quiz Models
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    module = models.ForeignKey(LearningModule, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Question Models
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text

# User Quiz Answer
class UserQuizAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return f"Answer for {self.quiz.title} by {self.user.username}"

# Scholarship Models
class Scholarship(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    eligibility_criteria = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Sponsorship Models
class Sponsorship(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    funding_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Student Performance Models
class StudentPerformance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    comments = models.TextField()
    tracked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Performance of {self.student.username} - {self.grade}"
