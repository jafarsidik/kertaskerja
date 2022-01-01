from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import loader
from django.conf.urls import url

# Create your views here.
from django.http import HttpResponse
#@login_required

def index(request):
    context = {'latest_question_list': "xxx"}
    
    return render(request, 'kertaskerja/dashboard.html', context)


def daftarsasaran(request):

    return render(request, 'daftar_sasaran/index.html')

def formdaftarsasaran(request):

    return render(request, 'kertaskerja/daftar_sasaran/index.html')
