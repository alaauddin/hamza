from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    tagline = models.TextField()
    bio = models.TextField()
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.name

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Skill Categories"
        ordering = ['order']

    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(default=100, help_text="Percentage 0-100")

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    tech_stack = models.CharField(max_length=500, help_text="Comma separated tech stack")
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100, default='Present')
    achievements = models.TextField(help_text="Bullet points describing key achievements")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-order']

    def __str__(self):
        return f"{self.role} at {self.company}"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-order']

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech_stack = models.CharField(max_length=500)
    link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-order']

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
