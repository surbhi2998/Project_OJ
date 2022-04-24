from django.contrib import admin
from .models import Items,User,Solutions,Problems

# Register your models here.
# class ItemsAdmin(admin.ModelAdmin):
#     pass
# class UserAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Items,ItemsAdmin)
# admin.site.register(User,UserAdmin)
@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    pass
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
@admin.register(Solutions)
class UserAdmin(admin.ModelAdmin):
    pass
@admin.register(Problems)
class UserAdmin(admin.ModelAdmin):
    pass

# Register your models here.
