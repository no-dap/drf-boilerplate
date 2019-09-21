from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=25)
    contents = models.TextField(blank=True)
    very_secret = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    contents = models.TextField()

    def __str__(self):
        return self.contents
