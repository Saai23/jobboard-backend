from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Change related_name to avoid clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Change related_name to avoid clash
        blank=True
    )

class JobListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Application(models.Model):
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    status = models.CharField(max_length=50, choices=[('applied', 'Applied'), ('interview', 'Interview'), ('hired', 'Hired'), ('rejected', 'Rejected')], default='applied')
    applied_at = models.DateTimeField(auto_now_add=True)
