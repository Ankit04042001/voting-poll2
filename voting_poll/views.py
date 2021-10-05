from django.shortcuts import redirect, render
from django.http import request, HttpResponse
from .models import Audio, TotalVote, Leader, UserIp
from django.contrib import messages
from django.contrib.sessions.backends.db import SessionStore
from django.db import transaction
from ipware import get_client_ip
# Create your views here.

def index(request):
    leader = Leader.objects.all()
    audio = Audio.objects.all()
    return render(request, 'index.html', {'leader':leader, 'audio':audio})


def dashboard(request):
    leader = Leader.objects.all()
    return render(request, 'dashboard.html', {'leader':leader})

@transaction.atomic
def vote(request):
    leader = Leader.objects.all()
    user_ip = get_client_ip(request)
    user_ip_list = UserIp.objects.all()
    ip_list = []
    for ip in user_ip_list:
        ip_list.append(ip.ip)
        print(ip.ip)

    already_voted = user_ip_list.filter(ip=user_ip)
    if already_voted:
        already_voted = True
    else:
        already_voted = False


    if request.method == 'POST':
        id = request.POST['id']
        totalVote = TotalVote.objects.get(pk=1)
        leader_vote = Leader.objects.get(pk=id)
        if (request.session.get('isVoted') == None) and (already_voted != True):
            request.session['isVoted'] = "yes"
            request.session.set_expiry(60*60*24*365)
            request.session.save()
            totalVote.total_vote += 1
            leader_vote.vote += 1
            totalVote.save()
            leader_vote.save()
            messages.success(request, 'Your Vote has been accepted.')
            UserIp(ip=user_ip).save()
        else:
            messages.error(request, 'You Voted already')
    return render(request, 'dashboard.html', {'leader':leader})

def csrf_failure(request, reason=""):
    ctx = {'message':'Please Enable cookie to vote and try again !'}
    return render(request,'cookie.html',ctx)


