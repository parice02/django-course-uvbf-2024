from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row

from app.models import Person


class PersonForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = "id-exampleForm"
    #     self.helper.form_class = "form-inline"
    #     self.helper.form_method = "post"
    #     self.helper.form_action = "submit_survey"
    #     self.helper.label_class = "col-lg-2"
    #     self.helper.field_class = "col-lg-8"
    #     self.helper.layout = Layout(Row("first_name", "last_name"), "age")

    #     self.helper.add_input(Submit("submit", "Soumettre"))

    

    class Meta:
        model = Person
        fields = ["first_name", "last_name", "age"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
        }
