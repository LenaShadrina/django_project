from django.db import models
from main_refs.models import Genre, Author, Series, Publishing_house
# Create your models here.


class Product(models.Model):
    title = models.CharField(
        verbose_name='Product title',
        max_length=200
    )
    cover = models.ImageField(
        verbose_name='Product cover',
        upload_to='product_covers/%Y/%m/%d/'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return ""


class Book(models.Model):
    name_book = models.CharField(max_length=200)
    image_cover = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="photo")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    authors = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="authors")
    series = models.ManyToManyField(Series)
    genres = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="genres")
    publication_date = models.DateField()
    pages = models.IntegerField(default=0)
    binding = models.CharField(max_length=200)
    format = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    weight = models.IntegerField(default=0)
    age_restriction = models.IntegerField(default=0)
    publishing_house = models.ForeignKey(Publishing_house, on_delete=models.PROTECT, related_name="publishing_house")
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name_book}"

