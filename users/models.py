from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=20, blank=True, null=True, unique=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

class UserModuleSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    module_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50, default='user')
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'module_name')

    def __str__(self):
        return f"{self.user.username} - {self.module_name} ({self.role})"
