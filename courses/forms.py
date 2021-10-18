from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateField
from courses.models import Course
from datetime import date


class PastMonthField(DateField):

    def validate(self, value):
        super().validate(value)
        if value <= date.today():
            raise ValidationError("Can't add course with past date")

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class FinishField(PastMonthField):

    def validate(self, value):
        super().validate(value)
        if value >= PastMonthField():
            raise ValidationError("Finish date need to be after start date obviously!")

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class NewCourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    starts = PastMonthField()
    finish = FinishField()
