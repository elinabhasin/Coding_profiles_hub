# profiles/models.py

from django.db import models

class UserProfile(models.Model):
    """
    Model to store user profile information.
    Fields include name, email, and links to coding profiles.
    """
    name = models.CharField(max_length=100, help_text="Full name of the user.")
    email = models.EmailField(unique=True, help_text="Unique email address of the user.")
    github = models.URLField(blank=True, null=True, help_text="URL to the user's GitHub profile.")
    leetcode = models.URLField(blank=True, null=True, help_text="URL to the user's LeetCode profile.")
    codeforces = models.URLField(blank=True, null=True, help_text="URL to the user's Codeforces profile.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the profile was created.")

    class Meta:
      
        ordering = ['-created_at']
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        """
        String representation of the UserProfile object.
        """
        return self.name

