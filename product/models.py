from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# class ProductManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter()


class Discount(models.Model):
    name = models.CharField(max_length=20)
    discount_percent = models.IntegerField()
    address = models.TextField()
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='static/img')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Qty = models.IntegerField()
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    # custom_object=ProductManager()

    def __str__(self):
        return self.name    

