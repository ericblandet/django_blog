from django.contrib import admin

from posts.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_at", "last_updated_at")
    # do not forget the , so that it is considered as a tuple:
    list_editable = ("published",)


admin.site.register(BlogPost, BlogPostAdmin)
