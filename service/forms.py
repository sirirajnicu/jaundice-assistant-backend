from django import forms

ROLE_CHOICES = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            {"name": "username", "class": "form-control", "placeholder": "Username"}
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            {"name": "password", "class": "form-control", "placeholder": "Password"}
        ),
    )
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        required=True,
        widget=forms.Select({"name": "role", "class": "form-control"}),
    )


class SearchForm(forms.Form):
    searchid = forms.CharField(
        required=True,
        widget=forms.TextInput(
            {"name": "searchid", "class": "form-control", "placeholder": "search"}
        ),
    )
