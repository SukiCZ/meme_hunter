from django.db import models


class Meme(models.Model):
    author = models.CharField(max_length=255)
    post_id = models.CharField('Reddit post ID', max_length=20)
    title = models.CharField(max_length=255)

    thumbnail = models.URLField()
    url = models.URLField()
