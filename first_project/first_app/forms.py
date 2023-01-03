from django import forms

class SearchForm(forms.Form):
    q = forms.CharField()

class TestForm(forms.Form):
    text = forms.CharField(min_length=7)
    boolean = forms.BooleanField()
    integer = forms.IntegerField()
    email = forms.EmailField()