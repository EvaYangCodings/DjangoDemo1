from django import forms

class SearchForm(forms.Form):
    q = forms.CharField()

class TestForm(forms.Form):
    text = forms.CharField(min_length=7)
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=10)
    email = forms.EmailField()

    def clean_integer(self):
        integer = self.cleaned_data.get("integer")
        if integer <= 10:
            raise forms.ValidationError("The integer should be greater than 10")
        return integer

    def clean_text(self):
        text = self.cleaned_data.get("text")
        if len(text) > 10:
            raise forms.ValidationError("The length of the text should between 7 and 10")
        return text