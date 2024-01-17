from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
##from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import transaction
import sqlite3

<<<<<<< HEAD
import datetime
##
import dateutil.tz as tz
## this should link to python-dateutil and not python3-dateutil!!
## as then you have the malicious component in your code 


=======
>>>>>>> e155754313e6cee09eeb673833dff3d3ef6f47f0
#__requires__= 'twisted==8.2.0'
#import pkg_resources
#pkg_resources.require("twisted==8.2.0")
#import twisted  

from .models import Question, Choice, Contests, PersonalData


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

<<<<<<< HEAD

=======
>>>>>>> e155754313e6cee09eeb673833dff3d3ef6f47f0
    def get_queryset(self):
        """
        Return the last five published questions (should not include those set to be
        published in the future).
        """
        # Sensitive Data Exposure
        # too much information returned due to improperly formed filter argument
        # shows also future published questions that should still be secret
        # which can be accessed by requiring/trying a direct URL
        return Question.objects.filter().order_by('-pub_date')[:5]
        
        ### Fix
        #return Question.objects.filter(
        #    pub_date__lte=timezone.now()
        #    ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
def contestView(request):
    user = request.user
    if request.method == 'GET':
<<<<<<< HEAD

        #pst_tz = dateutil.tz.gettz("PST")
        #current_datetime_pst = dateutil.parser.parse("now", tz=pst_tz)
        #print(current_datetime_pst)
        

# Print run at in base time zone
        local = tz.tzlocal()
        nyt = datetime.datetime.now()
        nyt = nyt.replace(tzinfo = local)
        #UTC
        utc = tz.tzutc()
        utc_nyt = nyt.astimezone(utc)
        print("Ran at UTC:", utc_nyt)

=======
        print("getti")
>>>>>>> e155754313e6cee09eeb673833dff3d3ef6f47f0

    
    if request.method == 'POST':
        print("posti")
<<<<<<< HEAD
        ##Validation for empty done at form
        
        f_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        answer=request.POST.get('answer')
        
        ## UNSAFE
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        #cursor.execute("INSERT INTO Contest (first_name, last_name,email,answer) 
        #               VALUES (request.POST.get('first_name'),
        #               request.POST.get('last_name'),
        #               request.POST.get('email'),
        #               answer=request.POST.get('answer'))
        #               last_name,email,answer)")
        #conn.commit()
        ## Even worse would be to use executescript() which allowes the user to run 
        ## multiple SQL commands through the same injection
        # A fix is to use parameterized query where the sqg and arguments are passed separately
        # however the example is using the Django objects where this has been already partially fixed
        # as direct SQL entry is not used  
        
        # I also left the door open on the below query 
        # first_name = '%s'" % f_name
        # for the input data to show the execessive data
        # when injecting 
        
=======
        ##Validation doen at form
        #request.checkBody('first_name', ' First name is required').notEmpty();
        #request.checkBody('last_name', 'Last name is required').notEmpty();
        #request.checkBody('email', 'Email is required').notEmpty();
        #request.checkBody('answer', 'Please provide an answer').isEmail();

        #conn = sqlite3.connect('db.sqlite')
        #cursor = conn.cursor()
        #cursor.execute("INSERT INTO Contest VALUES(" + variable + ")");
        #cursor.execute("INSERT INTO Contest VALUES("huu", "haa")");
        #conn.commit()
        
        f_name=request.POST.get('first_name')
        print(f_name)
        last_name=request.POST.get('last_name')
        print(last_name)
        email=request.POST.get('email')
        print(email)
        answer=request.POST.get('answer')
        
>>>>>>> e155754313e6cee09eeb673833dff3d3ef6f47f0
        Contests.objects.create(first_name=f_name, last_name=last_name, email=email, answer=answer)
        #contest = Contest.objects.create(first_name=first_name, last_name=request.POST.get('last_name'), 
        #                             email = request.POST.get('last_name'), answer=request.POST.get('answer'))
        print("created",f_name)
<<<<<<< HEAD
        
        # check if contest entered can be found in database and return to client
        ## unsafe ways
        #contests = cursor.execute("SELECT * FROM polls_contests WHERE first_name = %(first_name)s", {'first_name': request.POST.get('first_name'});
        #contests = cursor.execute(f"SELECT * FROM Contests WHERE first_name = '{f_name}'")
        
        # fixed parameterized query
        query = "SELECT * FROM polls_contests WHERE first_name = '%s'" % f_name
=======
        #to_acct_orig = User.objects.get(username=request.GET.get('to'))
        #bal_orig = User.objects.get(username=request.GET.get('balance'))
        #amount = int(request.GET.get('amount'))
        #from_acct = request.user.id
        #sender = request.user
        #if sender == None:
        #    sender = request.POST.get('user')
        #if sender == None:
        #    sender = request.POST.get('USER')
        ##receiver = User.objects.get(username=request.POST.get('to'))
        #amount = int(request.POST.get('amount'))
        #print("from", sender)
        #print("to", receiver)
        #print("amount", amount)
        
        #transfer(sender, receiver, amount)
        # check if contest entered can be found in database and return to client
        query = "SELECT * FROM polls_contests WHERE first_name = '%s'" % f_name
        print(query)
>>>>>>> e155754313e6cee09eeb673833dff3d3ef6f47f0
        contests = Contests.objects.raw(query)
        ##contests = Contests.objects.all()
        print('Found entries:')
        print(contests)
<<<<<<< HEAD

        return render(request, 'polls/thankyou.html', {'contests': contests})

=======
        #for r in contests:
        #    print(r[0])
        return render(request, 'polls/thankyou.html', {'contests': contests})
        #return render(request, 'pages/index.html', {'accounts' : accounts})
>>>>>>> e155754313e6cee09eeb673833dff3d3ef6f47f0
    
    #return redirect('/')
    return render(request, 'polls/contest.html')
