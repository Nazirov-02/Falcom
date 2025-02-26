from django import forms

class CommentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    review = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField