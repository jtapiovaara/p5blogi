from django import forms


class CommentForm(forms.Form):
    comment_author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nimesi"
            })
    )

    comment_body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Olen iloinen kommenteista!"
            })
    )
