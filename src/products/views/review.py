from django.shortcuts import render, redirect
from django.db.models import Avg

from products.forms.review_form import ReviewForm
from products.models import Review


def product_reviews_view(request):
    reviews = Review.objects.select_related('product', 'user').order_by('-created_at')

    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('product_reviews')
    else:
        form = ReviewForm()

    return render(request, 'products/product_reviews.html', {
        'form': form,
        'reviews': reviews,
        'average_rating': average_rating,
    })
