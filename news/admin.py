from django.contrib import admin

from .models import CustomUser,News,Comment,Category,Save

admin.site.register(CustomUser)
admin.site.register(News)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Save)