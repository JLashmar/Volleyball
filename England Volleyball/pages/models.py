from django.db import models

# Create your models here.


class PageCategory(models.Model):
    title = models.CharField(max_length=100, unique=False, default="default")
    category_slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=100, unique=False, default="default")
    page_slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(PageCategory, on_delete=models.PROTECT, default=1)
    body = models.TextField()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    # return reverse('articles:detail', kwargs={'category_slug': self.category.category_slug, 'page_slug': self.page_slug})
