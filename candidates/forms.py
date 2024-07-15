from candidates.models import Candidate
from users.froms import StyleFormMixin
from django import forms
from django.core.exceptions import ValidationError
from datetime import date


class CandidateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth:
            today = date.today()
            if date_of_birth > today:
                raise ValidationError("Дата рождения не может быть в будущем.")
            age = today.year - date_of_birth.year
            if today.month < date_of_birth.month or (
                    today.month == date_of_birth.month and today.day < date_of_birth.day):
                age -= 1
            if age <= 0:
                raise ValidationError("Возраст должен быть больше 0.")
        return date_of_birth
