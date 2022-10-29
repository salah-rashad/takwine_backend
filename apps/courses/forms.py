from django.forms import ModelForm

from apps.courses.models.question_choice import QuestionChoice

from .models.question import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'initial' in kwargs:
            self.fields['answer'].queryset = QuestionChoice.objects.filter(
                question=self.initial.question).order_by("ordering")
