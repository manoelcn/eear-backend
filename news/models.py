from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    date_publication = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='news/', blank=True, null=True)

    def __str__(self):
        return self.title
