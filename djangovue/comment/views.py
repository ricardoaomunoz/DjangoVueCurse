from django.shortcuts import render
from .models import Comment
from.forms import CommentForm
# Create your views here.

def index(request):
    comments = Comment.objects.all()

    return render(request,'index.html', {'comments':comments})


def add(request):

    form = CommentForm()
    return render(request, 'add.html', {"form": form})