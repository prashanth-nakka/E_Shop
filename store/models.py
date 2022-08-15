from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    description = models.TextField(default="", null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self) -> str:
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=500)

    # String Notation
    def __str__(self) -> str:
        return self.first_name

    # Saving the new User
    def register(self):
        self.save()

    # Email Validation
    def isEmail_exists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False
