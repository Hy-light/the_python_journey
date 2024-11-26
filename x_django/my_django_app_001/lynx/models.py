from django.db import models

# Create your models here.

class Article(models.Model):
    # attribute
    title = models.CharField(max_length=255)

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    # This is added to help return the title inputed
    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name_plural = "Blog posts"