from django.shortcuts import redirect, render
from django.http import request, HttpResponse
from .models import TotalVote, Leader
from django.contrib import messages
# Create your views here.

def index(request):
    leader = Leader.objects.all()
    return render(request, 'index.html', {'leader':leader})


def dashboard(request):
    leader = Leader.objects.all()
    return render(request, 'dashboard.html', {'leader':leader})

def vote(request):
    leader = Leader.objects.all()
    if request.method == 'POST':
        id = request.POST['id']
        totalVote = TotalVote.objects.get(pk=1)
        leader_vote = Leader.objects.get(pk=id)
        if request.session.get('isVoted') == None:
            request.session['isVoted'] = "yes"
            request.session.set_expiry(60*60*24*365)
            totalVote.total_vote += 1
            leader_vote.vote += 1
            totalVote.save()
            leader_vote.save()
            messages.success(request, 'Your Vote has been accepted.')
        else:
            messages.error(request, 'You Voted already')
    return render(request, 'dashboard.html', {'leader':leader})


