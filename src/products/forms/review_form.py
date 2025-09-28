from django import forms
from products.models.review import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'rating', 'comment']
        widgets = {
            'rating': forms.Select(),
            'comment': forms.Textarea(attrs={'rows': 4}),
        }
