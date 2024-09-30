from django import forms


class PersonForm(forms.Form):
    first_name = forms.CharField(
        max_length=10,
        label="Prénom",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        max_length=10,
        label="Nom",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    age = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))

    def clean_age(self):
        age = self.cleaned_data["age"]

        if age < 18:
            raise forms.ValidationError("Cette personne a moins de 18 ans")
        return age
