from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=200, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
            return reverse('products_by_category', args=[self.slug])  #for bringing in the url of the particular category clicked

    def __str__(self):
        return self.category_name


#<-- added coupon model
class Coupon(models.Model):
    coupon_code = models.CharField(max_length=100) 
    is_expired = models.BooleanField(default=True)
    discount_price = models.IntegerField(default=100)
    minimum_amount = models.IntegerField(default=500)

#coupon model ends -->


class MainCategory(models.Model):
    main_category_name = models.CharField(max_length=100,unique=True)
    slug               = models.SlugField(max_length=100,unique=True)
    description        = models.TextField(blank=True)

    class Meta:
        verbose_name       = 'Maincategory'
        verbose_name_plural= 'Maincategories'

    def get_url(self):
        return reverse('products_by_main_category',args=[self.slug])

    def __str__(self):
        return self.main_category_name



class SubCategory(models.Model):
    category          = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=100,unique=True)
    slug              = models.SlugField(max_length=100,unique=True)
    description       = models.TextField(blank=True)
    

    class Meta:
        verbose_name       = 'Subategory'
        verbose_name_plural= 'Subcategories'

    def get_url(self):
        return reverse('products_by_sub_category',args=[self.category.main_category.slug,self.category.slug,self.slug])

    def __str__(self):
        return self.category.main_category.main_category_name +'--' + self.category.category_name +'--' + self.sub_category_name