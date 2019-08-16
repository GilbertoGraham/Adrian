from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse
from django.shortcuts import render
import calendar;
import time;

from .services.QuestionService import QuestionService

questionService = QuestionService()


def index(request):
    return render(request, 'polls/index.html', questionService.loadQuestions())


def timestamp(request):
    ts = calendar.timegm(time.gmtime())
    response = JsonResponse({"timestamp": ts})
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response


def detail(request, question_id):
    question = questionService.loadQuestionById(question_id)
    if question is not None:
        return render(request, 'polls/detail.html', {'question': question})
    else:
        raise Http404("Question does not exist")


def results(request, question_id):
    question = questionService.loadQuestionById(question_id)
    if question is not None:
        return render(request, 'polls/results.html', {'question': question})
    else:
        raise Http404("Question does not exist")

def vote(request, question_id):
    try:
        if 'choice' in request.POST:
            choice = request.POST['choice']
            questionService.voteChoice(question_id, choice)
            return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
        else:
            raise Exception
    except Exception:
        return render(request, 'polls/detail.html', {
            'question': questionService.loadQuestionById(question_id),
            'error_message': "You didn't select a choice.",
        })
