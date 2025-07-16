from django.db import models
import string, random

def generate_shortcode():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class ShortURL(models.Model):
    url = models.URLField()
    shortCode = models.CharField(max_length=6, unique=True, default=generate_shortcode)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    accessCount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.shortCode} -> {self.url}"
