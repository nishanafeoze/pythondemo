from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView
class Tasklisitview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'

class TaskDetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')





def home(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task=Task(name=name,priority=priority,date=date)
        task.save()

    return render(request,'home.html',{'task1':task1})
# def details(request):
#
#     return render(request,'details.html')
def delete(request, id):
    if request.method == "POST":
        movie = Task.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
def update(request, id):
    task = Task.objects.get(id=id)
    form =TodoForm(request.POST or None, request.FILES, instance=task)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'task': task})

def get_success_url(self):
    return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
