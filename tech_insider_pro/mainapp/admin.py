from django.contrib import admin
from .models import Post, ContactMessage, TopPick, Advertisement


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "post_type", "category", "published_at", "active")
    list_filter = ("post_type", "category", "active")
    search_fields = ("title", "category", "content")
    prepopulated_fields = {"slug": ("title",)}

    # Add 'published_at' to the main edit screen
    fieldsets = (
        (
            None,
            {"fields": ("title", "slug", "post_type", "category", "excerpt", "content", "featured_image")},
        ),
        ("Publishing", {"fields": ("published_at", "active")}),
    )

    date_hierarchy = "published_at"
    ordering = ("-published_at",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")

@admin.register(TopPick)
class TopPickAdmin(admin.ModelAdmin):
    list_display = ("title", "price_text", "active", "priority")
    list_editable = ("active", "priority")
    ordering = ("priority",)


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "active", "created_at")
    readonly_fields = ("created_at",)

from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'created_at')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'content', 'pros', 'cons')
    list_filter = ('rating', 'created_at')
