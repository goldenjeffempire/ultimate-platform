from django.db import models

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
