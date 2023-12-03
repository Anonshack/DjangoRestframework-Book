from django.db import models
from django.utils import timezone
# Create your models here.


class Auther(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    biography = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=100)
    auther = models.ForeignKey(Auther, on_delete=models.CASCADE, related_name='book_auther')
    publish_date = models.DateTimeField(default=timezone.now)
    year = models.IntegerField()
    image = models.ImageField(upload_to='books/', blank=True, null=True)
    info = models.TextField(verbose_name='Info\'s book')
    price = models.FloatField()

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='book_review')
    reviewer_name = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    rate = models.IntegerField(verbose_name='Rate')

    def __str__(self):
        return str(self.book) + ' : ' + str(self.content)