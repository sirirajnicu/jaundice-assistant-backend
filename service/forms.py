from django import forms


ROLE_CHOICES = (
    ("P", "Pediatrician"),
    ("PN", "Postpartum Nurse"),
    ("NN", "Neonatal Nurse"),
    ("MS", "Medical Student"),
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
            {
                "name": "searchid",
                "class": "form-control",
                "placeholder": "Hospital Number",
            }
        ),
    )


class BabyInfoForm(forms.Form):
    firstname = forms.CharField(
        widget=forms.TextInput(
            {"name": "firstname", "class": "form-control", "placeholder": "First name"}
        ),
    )
    lastname = forms.CharField(
        widget=forms.TextInput(
            {"name": "lastname", "class": "form-control", "placeholder": "Last name"}
        ),
    )
    bd = forms.DateField(
        widget=forms.DateInput(
            {
                "name": "Birth date",
                "class": "form-control",
                "placeholder": "Birth date",
                "type": "date",
            }
        ),
    )
    time = forms.TimeField(
        widget=forms.TimeInput(
            {
                "name": "Birth time",
                "class": "form-control",
                "placeholder": "Birth time",
                "type": "time",
            }
        ),
    )
    bw = forms.CharField(
        widget=forms.TextInput(
            {
                "name": "Birth weight",
                "class": "form-control",
                "placeholder": "Birth weight",
            }
        ),
    )
    HN = forms.CharField(
        widget=forms.TextInput(
            {"name": "HN", "class": "form-control", "placeholder": "HN"}
        ),
    )
    GA = forms.CharField(
        widget=forms.TextInput(
            {"name": "GA", "class": "form-control", "placeholder": "GA"}
        ),
    )
    AN = forms.CharField(
        widget=forms.TextInput(
            {"name": "AN", "class": "form-control", "placeholder": "AN"}
        ),
    )
    AT = forms.ChoiceField(
        choices=(("", "-"), ("birth", "birth"), ("readmit", "readmit")),
        widget=forms.Select(
            {"name": "AT", "class": "form-control", "placeholder": "Admission type"}
        ),
        initial="",
        required=True,
    )
