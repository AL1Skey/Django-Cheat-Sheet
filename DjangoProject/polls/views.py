from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Quest,Option

# Create your views here.

def index(request):
    latest_polls = Quest.objects.order_by('pub_date')[:5]# Get Quest models object in database and order by published date until the list reach by 5
    context = {'polls_database':latest_polls}# Create dictonary based of latest_polls and add to html template as polls_database
    return render(request,'polls/index.html',context)# Insert request and context to polls/index.html

def test(request):
    return render(request,'testing/test.html')

def root(request):
    return render(request,'root/index.html')

#Show specific question and choice
def details(request,question_id):
    try:
        question = Quest.objects.get(pk=question_id)
    except Quest.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/result.html',{'question':question})

def result(request,question_id):
    question = get_object_or_404(Quest,pk=question_id) #this is same ase try execpt above
    return render(request,'polls/result.html',{'question':question})    
