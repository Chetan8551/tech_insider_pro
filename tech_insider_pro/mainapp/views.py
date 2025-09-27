from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Post, TopPick, Advertisement, Review
from .forms import ContactForm

# Synonyms mapping for search terms
SYNONYM_CATEGORY_MAP = {
    "horror": ["horror"],
    "ghost": ["horror"],
    "scary": ["horror"],
    "ai": ["ai", "ai tools", "artificial intelligence", "technology", "tech"],
    "artificial": ["ai", "artificial intelligence"],
    "tech": ["technology", "tech", "software", "ai"],
    "software": ["software", "applications"],
}

def home(request):
    top_picks = TopPick.objects.filter(active=True).order_by('priority')[:3]

    # ✅ Latest posts (articles & guides only)
    latest_posts = Post.objects.filter(
        post_type__in=['article', 'guide'], active=True
    ).order_by('-published_at')[:6]

    # ✅ Latest reviews from Review model
    latest_reviews = Review.objects.order_by('-created_at')[:3]

    ad_banner = Advertisement.objects.filter(position='home_banner', active=True).first()

    context = {
        'top_picks': top_picks,
        'latest_posts': latest_posts,
        'latest_reviews': latest_reviews,
        'ad_banner': ad_banner,
    }
    return render(request, 'mainapp/home.html', context)


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
            query |= Q(title__icontains=term) | Q(content__icontains=term) | Q(category__icontains=term)
            if term in SYNONYM_CATEGORY_MAP:
                for cat_substr in SYNONYM_CATEGORY_MAP[term]:
                    query |= Q(category__icontains=cat_substr)
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


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mainapp/post_detail.html', {'post': post})


def review_detail(request, slug):
    review = get_object_or_404(Review, slug=slug)
    return render(request, "mainapp/review_detail.html", {"review": review})


def about(request):
    return render(request, 'mainapp/about.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, "mainapp/contact.html", {"form": form})


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            messages.error(request, "Please provide an email address.")
            return redirect(request.META.get('HTTP_REFERER', 'mainapp:blog'))
        try:
            from .models import Subscription
            sub, created = Subscription.objects.get_or_create(email=email)
            if created:
                messages.success(request, "Subscribed — thank you!")
            else:
                messages.info(request, "You're already subscribed.")
        except Exception:
            messages.success(request, "Subscribed (note: not stored — no Subscription model found).")
        return redirect(request.META.get('HTTP_REFERER', 'mainapp:blog'))
    return redirect('mainapp:blog')


def disclaimer(request):
    return render(request, 'mainapp/disclaimer.html')
