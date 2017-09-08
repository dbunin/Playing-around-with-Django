from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    pubDate = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return 'Post: ' + self.title

    def getDate(self):
        return self.pubDate.strftime('%b %e %Y')

    def summary(self):
        if len(self.body) < 200:
            return self.body
        else:
            return self.body[:200] + '...'
