from .models import Student

from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class Teacher(forms.Form):
    name1 = forms.CharField(max_length=11, min_length=4)
