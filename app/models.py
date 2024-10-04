from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


def validate_min_age(value):
    if value < 18:
        raise ValidationError("Cette personne a moins de 18 ans")


class Person(models.Model):
    first_name = models.CharField(
        "Prénom", max_length=50, validators=[RegexValidator(regex=r"^[a-z]+$")]
    )
    last_name = models.CharField("Nom", max_length=50)
    age = models.SmallIntegerField("Âge", validators=[validate_min_age])
