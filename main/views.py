from django.shortcuts import render, redirect
from .models import Task
from .form import TaskForm
# Create your views here.


def index(request):
    tasks = Task.objects.all()
    return render(request, "main/index.html", {'title': 'Main page of the web site', 'tasks': tasks})


def about(request):
    return render(request, "main/about.html")


def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not correct'
    form = TaskForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, "main/create.html", context)


def delete(request):
    if request.method == "POST":
        id = int(request.POST.get('id'))
        try:
            item = Task.objects.get(pk=id)
            item.delete()
            return redirect('home')
        except:
            pass
    tasks = Task.objects.all()
    return render(request, "main/delete.html", {'tasks': tasks})