from django.http import HttpResponse
from .models import Questions


def index(request):
    latest_questions=Questions.objects.order_by('pub_date')[:5]
    output=','.join([q.question_text for q in latest_questions])
    return HttpResponse(output)

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." %question_id)

def results(request,question_id):
    return HttpResponse("Your're looking at the results for the questin %s." %question_id)

def votes(request,question_id):
    return HttpResponse("You are voting on the question %s." %question_id)
