from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
import math

TYPE_CHOICES = [
    ("article", "Article"),
    ("review", "Review"),
    ("guide", "Guide"),
]

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    post_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default="article"
    )

    category = models.CharField(max_length=120, blank=True)

    excerpt = models.TextField(blank=True)

    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)

    content = CKEditor5Field("Content", config_name="default")

    featured_image = models.ImageField(upload_to="posts/", blank=True, null=True)

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-published_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        if not self.meta_title:
            self.meta_title = self.title[:70]

        if not self.meta_description:
            self.meta_description = self.excerpt[:160] if self.excerpt else self.title[:160]

        super().save(*args, **kwargs)

    @property
    def reading_time(self):
        text = str(self.content)
        words = len(text.split())
        return max(1, math.ceil(words / 200))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("mainapp:post_detail", kwargs={"pk": self.pk, "slug": self.slug})


class TopPick(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, blank=True)
    price_text = models.CharField(max_length=80, blank=True)
    cta_text = models.CharField(max_length=40, default="Buy Now")
    cta_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='top_picks/', blank=True, null=True)
    active = models.BooleanField(default=True)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Advertisement(models.Model):
    POSITION_CHOICES = [
        ('home_banner', 'Home Banner'),
        ('sidebar_1', 'Sidebar 1'),
        ('in_content', 'In Content'),
    ]

    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='ads/', blank=True, null=True)
    script = models.TextField(blank=True)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, default='home_banner')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.TextField(blank=True, null=True)
    content = models.TextField()

    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    pros = models.TextField(blank=True, null=True)
    cons = models.TextField(blank=True, null=True)

    featured_image = models.ImageField(upload_to="reviews/", blank=True, null=True)
    affiliate_link = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title