from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request) : 
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})

def results(request, question_id):
    return HttpResponse(f"You are looking at the result of the Questiuon number {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You are voting on question ID {question_id}")

