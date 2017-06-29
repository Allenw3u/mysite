from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from .models import Question,Choice
from django.views import generic
from django.template import loader
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.)