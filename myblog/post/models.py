from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField()

class Comment(models.Model):
    writerNAme = models.CharField(max_length=20)
    writerEmail = models.CharField(max_length=20)
    message = models.TextField()
    date = models.DateTimeField()
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    

