from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField('Title', max_length=156)
    content = models.TextField('Content')
    date_of_publication = models.DateTimeField('Date_of_publication', auto_now_add=True)
    date_of_change = models.DateTimeField('Date_of_change', auto_now=True)
    is_published = models.BooleanField('Published', default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Category(models.Model):
    category_name = models.CharField('Category', max_length=50, db_index=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
