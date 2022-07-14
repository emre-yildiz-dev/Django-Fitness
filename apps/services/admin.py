from django.contrib import admin
from .models import Image, Service, Category, Comment


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "category", "price")


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment', 'ipaddress')


class ImageAdmin(admin.ModelAdmin):
    list_display = ("title",)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Category)
admin.site.register(Image, ImageAdmin)
