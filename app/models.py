from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    backgroundImage = models.ImageField(upload_to="uploads/restaurants/background/",blank=True, null=True)

    def __str__(self):
        return self.name

class MenuCategory(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.restaurant.name}/{self.name}'

class Orderable(models.Model):
    class Meta:
        abstract = True
    price = models.FloatField(default=0)

class Menu(Orderable):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="uploads/menus/images/", blank=True, null=True)
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f'{self.menu_category}/{self.name}'
    # https://books.agiliq.com/projects/django-admin-cookbook/en/latest/nested_inlines.html

    def save(self, *args, **kwargs):
        self.restaurant = self.menu_category.restaurant
        super().save(*args, **kwargs)

class MenuOption(Orderable):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=500, blank=True, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True)
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.menu}/{self.name}'

    def save(self, *args, **kwargs):
        self.menu_category = self.menu.menu_category
        self.restaurant = self.menu_category.restaurant
        super().save(*args, **kwargs)

