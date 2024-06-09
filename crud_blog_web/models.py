from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, blank=False, unique=False)
    content = models.TextField(blank=False, default='')
    year = models.PositiveSmallIntegerField(default=2023)
    image = models.ImageField(upload_to='media',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_with_year()

    def title_with_yera(self):
        return "{} ({})".format(self.title, self.year)

class Meta:
    verbose_name = "Article"
    verbose_name_plural = "Artykuły"
