from django import forms
from dashboard.models import BooksOfUsers

rating_choices = [tuple([x, x]) for x in range(1, 11)]


status_choices = [tuple([x, x]) for x in ['Nie wybrano', 'Do przeczytania', 'Przeczytana', 'Porzucona']]


class RatingForm(forms.Form):
    rating = forms.IntegerField(label="Ocena", widget=forms.Select(choices=rating_choices))


class StatusForm(forms.Form):
    status = forms.ChoiceField(label="", choices=status_choices, widget=forms.Select(attrs={'class': 'form-control status_select'}))
