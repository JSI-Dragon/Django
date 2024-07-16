from django.db import models

class Object(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='objects/images/')
    release_date = models.DateField()
    video_url = models.URLField(blank=True)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)