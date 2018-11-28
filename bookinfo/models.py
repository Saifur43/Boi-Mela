from django.db import models
from django.utils.text import slugify

class Publisher(models.Model):
    p_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.p_name

class Author(models.Model):
    a_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.a_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    image = models.ImageField(upload_to='images/',blank=True)
    slug = models.SlugField(max_length=250, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Book, self).save(*args, **kwargs)

class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()