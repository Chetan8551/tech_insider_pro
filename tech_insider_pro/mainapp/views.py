
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponse

from .models import Post, TopPick, Advertisement, Review
from .forms import ContactForm


# ==========================================
# SEARCH SYNONYMS
# ==========================================

SYNONYM_CATEGORY_MAP = {
    "horror": ["horror"],
    "ghost": ["horror"],
    "scary": ["horror"],
    "ai": ["ai", "ai tools", "artificial intelligence", "technology", "tech"],
    "artificial": ["ai", "artificial intelligence"],
    "tech": ["technology", "tech", "software", "ai"],
    "software": ["software", "applications"],
}


# ==========================================
# HOME
# ==========================================

def home(request):
    top_picks = TopPick.objects.filter(active=True).order_by('priority')[:3]

    latest_posts = Post.objects.filter(
        post_type__in=['article', 'guide'],
        active=True
    ).order_by('-published_at')[:6]

    latest_reviews = Review.objects.order_by('-created_at')[:3]

    ad_banner = Advertisement.objects.filter(
        position='home_banner',
        active=True
    ).first()

    context = {
        'top_picks': top_picks,
        'latest_posts': latest_posts,
        'latest_reviews': latest_reviews,
        'ad_banner': ad_banner,
    }

    return render(request, 'mainapp/home.html', context)


# ==========================================
# BLOG
# ==========================================

def blog(request):
    q = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()

    posts_qs = Post.objects.filter(active=True)

    if category:
        posts_qs = posts_qs.filter(category__iexact=category)

    if q:
        terms = [t.lower() for t in q.split() if t]
        query = Q()

        for term in terms:
            query |= (
                Q(title__icontains=term) |
                Q(content__icontains=term) |
                Q(category__icontains=term)
            )

            if term in SYNONYM_CATEGORY_MAP:
                for synonym in SYNONYM_CATEGORY_MAP[term]:
                    query |= Q(category__icontains=synonym)

        posts_qs = posts_qs.filter(query)

    posts_qs = posts_qs.order_by('-published_at')

    categories = (
        Post.objects.filter(active=True)
        .values_list('category', flat=True)
        .exclude(category__isnull=True)
        .exclude(category__exact='')
        .distinct()
    )

    paginator = Paginator(posts_qs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'categories': categories,
        'active_category': category or None,
        'query': q,
    }

    return render(request, 'mainapp/blog.html', context)


# ==========================================
# POST DETAIL
# ==========================================

def post_detail(request, pk, slug):
    post = get_object_or_404(
        Post,
        pk=pk,
        slug=slug,
        active=True
    )

    related_posts = Post.objects.filter(
        category=post.category,
        active=True
    ).exclude(pk=post.pk).order_by('-published_at')[:3]

    in_content_ad = Advertisement.objects.filter(
        position='in_content',
        active=True
    ).first()

    context = {
        'post': post,
        'related_posts': related_posts,
        'in_content_ad': in_content_ad,
    }

    return render(request, 'mainapp/post_detail.html', context)


# ==========================================
# REVIEW DETAIL
# ==========================================

def review_detail(request, slug):
    review = get_object_or_404(Review, slug=slug)

    related_reviews = Review.objects.exclude(
        pk=review.pk
    ).order_by('-created_at')[:3]

    context = {
        'review': review,
        'related_reviews': related_reviews,
    }

    return render(request, 'mainapp/review_detail.html', context)


# ==========================================
# STATIC PAGES
# ==========================================

def about(request):
    return render(request, 'mainapp/about.html')


def disclaimer(request):
    return render(request, 'mainapp/disclaimer.html')


def privacy_policy(request):
    return render(request, 'mainapp/privacy_policy.html')


def affiliate_disclosure(request):
    return render(request, 'mainapp/affiliate_disclosure.html')


def terms_conditions(request):
    return render(request, 'mainapp/terms_conditions.html')


# ==========================================
# CONTACT
# ==========================================

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your message has been sent successfully!"
            )

            return redirect('mainapp:contact')

    else:
        form = ContactForm()

    return render(request, 'mainapp/contact.html', {'form': form})


# ==========================================
# SUBSCRIBE
# ==========================================

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if not email:
            messages.error(
                request,
                "Please provide an email address."
            )

            return redirect(
                request.META.get(
                    'HTTP_REFERER',
                    'mainapp:blog'
                )
            )

        messages.success(
            request,
            "Subscribed successfully!"
        )

        return redirect(
            request.META.get(
                'HTTP_REFERER',
                'mainapp:blog'
            )
        )

    return redirect('mainapp:blog')


# ==========================================
# ROBOTS.TXT
# ==========================================

def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Allow: /",
        "Sitemap: https://yourdomain.com/sitemap.xml"
    ]

    return HttpResponse(
        "\n".join(lines),
        content_type="text/plain"
    )


# ==========================================
# SITEMAP.XML
# ==========================================

def sitemap_xml(request):
    posts = Post.objects.filter(active=True)

    return render(
        request,
        'mainapp/sitemap.xml',
        {'posts': posts},
        content_type='application/xml'
    )

