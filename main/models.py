from distutils.command.upload import upload
from statistics import mode
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from autoslug import AutoSlugField
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'cat_img', null = True, blank = True)
    slug =  AutoSlugField(populate_from='title', editable = True)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=200)
	slug = AutoSlugField(populate_from='title')

	def __str__(self):
		return self.title

class Product(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200)
	category =models.ForeignKey(Category, on_delete=models.CASCADE)
	subcategory =models.ForeignKey(SubCategory, on_delete=models.CASCADE)
	image = models.FileField(upload_to='products/')
	price = models.FloatField(default=0)
	slug =  AutoSlugField(populate_from='name')
	description = models.TextField()
	quantity = models.IntegerField(default=0)
	contact = models.BigIntegerField(null=True, blank=True)
	view_count = models.PositiveIntegerField(default=0)
	date_created = models.DateTimeField(default=now)


	def __str__(self):
		return self.name

class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='products.image/')

	def __str__(self):
		return self.product.name
	

class Review(models.Model):
    review = models.TextField()
    name = models.CharField(max_length = 56)
