from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoItemForm

def index(request):
    todos = TodoItem.objects.all()
    form = TodoItemForm()
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'todo/index.html', {'todos': todos, 'form': form})

def edit_todo(request, id):
    todo = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'todo/edit_todo.html', {'form': form})

def delete_todo(request, id):
    todo = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    return render(request, 'todo/delete_todo.html', {'todo': todo})
