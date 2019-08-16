from django.http import Http404
from django.views import View
from django.shortcuts import render
from ..services.QuestionService import QuestionService

class QuestionView(View):
    def __init__(self):
        self.questionService = QuestionService()

    def get(self, request, question_id):
        question = self.questionService.loadQuestionById(question_id)
        if question is not None:
            return render(request, self.template_name, {'question': question})
        else:
            raise Http404("Question does not exist")

class QuestionDetailView(QuestionView):
    template_name = 'polls/detail.html'

class QuestionResponseView(QuestionView):
    template_name = 'polls/results.html'