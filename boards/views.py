from django.shortcuts import render
from django.http import Http404
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
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})
