from django.contrib import admin
from instagrm.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    filter_horizontal =('comments',)

# Register your models here.
admin.site.register(Post, admin_class=PostAdmin)
admin.site.register(Comment)