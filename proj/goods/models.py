from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(
        verbose_name='Product title',
        max_length=200
    )
    cover = models.ImageField(
        verbose_name='Product cover',
    )
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return ""


#class Book(models.Model):
    #title_book = models.CharField(max_length=200)
    #photo_cover = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="photo")
    #genres = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="genres")
    #authors = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="authors")
    #series = models.ManyToManyField(Series)
    #publishing_house = models.ForeignKey(Publishing_house, on_delete=models.PROTECT, related_name="publishing_house")
    #publication_date = models.DateField()
    #pages = models.IntegerField(default=0)
    #price = models.DecimalField(max_digits=5, decimal_places=2)
    #description = models.TextField(
        #blank=True,
        #null=True
    #)

    #def __str__(self):
        #return f"{self.title}"

    #def get_absolute_url(self):
        #return f"/author-detail-cbv/{self.pk}/"