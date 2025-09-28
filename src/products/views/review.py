from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.forms.review_form import ReviewForm
from products.models import Review, Product
from common_services.permissions.login_permissions import login_required_redirect


def product_reviews_view(request):
    reviews = Review.objects.select_related('product', 'user').order_by('-created_at')

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
        'reviews': reviews
    })
