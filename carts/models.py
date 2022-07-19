from django.db import models
from accounts.models import Account
from category.models import Coupon

from store.models import Product, Variation

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250)
    # coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True) #added coupon from category model
    date_added = models.DateField(auto_now_add=True)
    razor_pay_order_id = models.CharField(max_length=100, null=True, blank=True)
    razor_pay_payment_id = models.CharField(max_length=100, null=True, blank=True)
    razor_pay_payment_signature = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product

    