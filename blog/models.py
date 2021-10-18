from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)
    signature = models.CharField(max_length=64, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    content = models.TextField()
    signature = models.CharField(max_length=64, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
