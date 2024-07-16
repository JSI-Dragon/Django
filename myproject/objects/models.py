from django.db import models

class Object(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='objects/images/')
    release_date = models.DateField()
    video_url = models.URLField(blank=True)

    def __str__(self):
        return self.name