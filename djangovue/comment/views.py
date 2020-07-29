from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from.forms import CommentForm, ContactForm
# Create your views here.

def index(request):
    comments = Comment.objects.all()

    return render(request,'index.html', {'comments':comments})


def add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CommentForm()
    return render(request, 'add.html', {"form": form})


def update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save(commit=True)
            return redirect('update', pk=comment.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'update.html', {"form": form, 'comment': comment})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})
