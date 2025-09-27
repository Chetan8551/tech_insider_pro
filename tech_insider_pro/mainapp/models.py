from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse


TYPE_CHOICES = [
    ("article", "Article"),
    ("review", "Review"),
    ("guide", "Guide"),
]


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    post_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="article")
    category = models.CharField(max_length=120, blank=True)
    excerpt = models.TextField(blank=True)
    content = CKEditor5Field("Content", config_name="default")
    featured_image = models.ImageField(upload_to="posts/", blank=True, null=True)

    # keep created_at (when the DB record was created)
    created_at = models.DateTimeField(auto_now_add=True)

    # editable in admin so you can change it manually
    published_at = models.DateTimeField(
        default=timezone.now,
        blank=True,
        null=True,
        help_text="Date/time shown on the site. You can edit this in the admin.",
    )

    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-published_at"]

    def save(self, *args, **kwargs):
        # auto-generate a slug if it's empty
        if not self.slug and self.title:
            base = slugify(self.title)[:250]
            slug = base
            i = 0
            # ensure unique slug (exclude self when updating)
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f"{base}-{i}"
                if len(slug) > 255:
                    slug = slug[:250] + str(i)
            self.slug = slug

        # if published_at is not provided, default it to created_at if exists else now
        if not self.published_at:
            if self.pk and hasattr(self, "created_at") and self.created_at:
                self.published_at = self.created_at
            else:
                self.published_at = timezone.now()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("mainapp:post_detail", kwargs={"pk": self.pk, "slug": self.slug})



class TopPick(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, blank=True)
    price_text = models.CharField(max_length=80, blank=True)      # e.g. "$1,599" or "$20/mo"
    cta_text = models.CharField(max_length=40, default="Buy Now")
    cta_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='top_picks/', blank=True, null=True)
    active = models.BooleanField(default=True)
    priority = models.IntegerField(default=0)  # order by priority asc

    def __str__(self):
        return self.title


class Advertisement(models.Model):
    POSITION_CHOICES = [
        ('home_banner', 'Home banner'),
        ('sidebar_1', 'Sidebar 1'),
    ]
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='ads/', blank=True, null=True)
    script = models.TextField(blank=True, help_text="Put ad script (AdSense) here if not using image")
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, default='home_banner')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
    

class Review(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.TextField(blank=True, null=True)
    content = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # 0.0 → 5.0
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