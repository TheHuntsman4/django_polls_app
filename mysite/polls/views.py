from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Questions,Choice
from django.shortcuts import render,get_object_or_404
from django.urls import  reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_questions'

    def get_queryset(self):
        return Questions.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model=Questions
    template_name='polls/details.html'



# def detail(request,question_id):
#     try:
#         question=Questions.objects.get(pk=question_id)
#     except Questions.DoesNotExist:
#         raise Http404("Question does not exists")
#     return render(request,'polls/details.html',{'question':question}) 


class ResultsView(generic.DetailView):
    model=Questions
    template_name='polls/results.html'


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
