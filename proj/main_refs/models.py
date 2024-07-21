from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    author = models.CharField(max_length=200)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name="author"
    )
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.author} #{self.pk}"

    def get_absolute_url(self):
        return f"/author-detail-cbv/{self.pk}/"


class Series(models.Model):
    pocket_book = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.pocket_book}"


class Publishing_house(models.Model):
    publishing = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.publishing}"


#class Book(models.Model):
    #title_book = models.CharField(max_length=200)
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