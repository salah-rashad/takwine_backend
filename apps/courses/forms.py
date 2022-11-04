from django.forms import ModelForm

from apps.courses.models.question_choice import QuestionChoice

from .models.question import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        answer = self.instance.answer
        answerField = self.fields['answer']

        if answer is None:
            answerField.help_text = "🛑 Answer is not assigned"

        if answerField:
            answerField.queryset = self.get_choices()

    def get_choices(self):
        return QuestionChoice.objects.filter(
            question=self.instance).order_by("ordering")
