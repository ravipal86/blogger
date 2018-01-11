from django.shortcuts import render
from django.http import HttpResponse
from boards.models import Board


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def about(request):
    return render(request, 'about.html')


def about_company(request):
    context = {'company_name': 'Simple Complex'}
    return render(request, 'about_company.html', context)


def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})
