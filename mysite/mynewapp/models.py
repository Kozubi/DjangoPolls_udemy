from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    sec_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return "{} {}".format(self.name, self.sec_name)

class Book(models.Model):
    title = models.CharField(max_length=255)
    publ_date = models.DateField()
    genere = models.CharField(max_length=255)
    count = models.IntegerField()
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.title



