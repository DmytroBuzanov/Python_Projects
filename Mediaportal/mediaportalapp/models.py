from __future__ import unicode_literals
from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField()

    """def __unicode__(self):
        return self.name"""

    def __str__(self):
        return self.name

class ArticleManager(models.Manager):

    def all(self, *args, **kwargs):
        return super(ArticleManager, self).get_queryset().filter(pk__in=[3, 5, 7])

def generate_filename(instance, filename):
    filename = instance.slug + '.jpg'
    return "{0}/{1}".format(instance, filename)

class Article(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # on_delete=models.CASCADE добавил сам
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    image = models.ImageField(upload_to=generate_filename)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    objects = models.Manager()
    custom_manager = ArticleManager()

    def __str__(self):
        return "Статья '{0}' из категории '{1}'".format(self.title, self.category.name)

class MyArticles(Article):

    class Meta:
        proxy = True
