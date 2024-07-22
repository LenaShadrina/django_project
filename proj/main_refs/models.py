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


