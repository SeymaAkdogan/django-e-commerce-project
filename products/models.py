from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="categoryImage")
    category_slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.category_slug = slugify(self.name)
        super().save(*args,**kwargs)


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    image = models.ImageField(upload_to="productsImage")
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    categories = models.ManyToManyField(Category,blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

