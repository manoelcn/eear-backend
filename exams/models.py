from django.db import models


class Exam(models.Model):
    title = models.CharField(max_length=100)
    date_publication = models.DateTimeField(auto_now_add=True)    
    description = models.CharField(max_length=500)
    file = models.FileField(upload_to='exam/')

    def __str__(self):
        return self.title
