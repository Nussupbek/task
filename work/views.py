from django.shortcuts import render, redirect, reverse
from .models import Artiсles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def work_home(request):
    work = Artiсles.objects.all()
    return render(request, 'work/work_home.html', {'work': work})

class WorkDetailView(DetailView):
    model = Artiсles
    template_name = 'work/details_view.html'
    context_object_name = 'article'

class WorkUpdateView(UpdateView):
    model = Artiсles
    template_name = 'work/create.html'
    form_class = ArticlesForm

class WorkDeleteView(DeleteView):
    model = Artiсles
    success_url = '/work/'
    template_name = 'work/work-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/work/')
        else:
            error = 'Форма задачи была неправильно заполнена'

    form = ArticlesForm()

    data={
        'form': form,
        'error': error
    }

    return render(request, 'work/create.html', data)
