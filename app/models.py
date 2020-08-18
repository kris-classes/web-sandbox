from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=256)
    duration = models.IntegerField()
    description = models.TextField()
    picture = models.ImageField(blank=True)
    genre = models.ManyToManyField('Genre')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    create_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Video: {self.title}'


class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'Genre: {self.name}'


class Action(models.Model):
    name = models.CharField(max_length=256)


class Category(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return f'Category: {self.name}'


