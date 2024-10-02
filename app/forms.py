from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row


class PersonForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-exampleForm"
        self.helper.form_class = "form-inline"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_survey"
        self.helper.label_class = "col-lg-2"
        self.helper.field_class = "col-lg-8"
        self.helper.layout = Layout(Row("first_name", "last_name"), "age")

        self.helper.add_input(Submit("submit", "Soumettre"))

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
