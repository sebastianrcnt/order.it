from django.contrib import admin
from .models import *

# inlines
class MenuCategoryInline(admin.StackedInline):
    model = MenuCategory
    extra = 0

class MenuInline(admin.StackedInline):
    model = Menu
    extra = 0

class MenuOptionInline(admin.StackedInline):
    model = MenuOption
    extra = 0

class RestaurantAdmin(admin.ModelAdmin):
    inlines = [
        MenuCategoryInline,
        MenuInline,
        MenuOptionInline,
    ]    
admin.site.register(Restaurant, RestaurantAdmin)

class MenuCategoryAdmin(admin.ModelAdmin):
    inlines = [
        MenuInline,
        MenuOptionInline,
    ]
admin.site.register(MenuCategory, MenuCategoryAdmin)

class MenuAdmin(admin.ModelAdmin):
    inlines = [
        MenuOptionInline,
    ]
admin.site.register(Menu, MenuAdmin)



# Register your models here.
admin.site.register(MenuOption)