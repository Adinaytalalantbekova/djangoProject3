from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from . import models, forms


def shows_all(request):
    shows = models.TVShow.objects.all()
    return render(request, 'shows_list.html',
                  {'shows': shows})


def shows_detail(request, id):
    show = get_object_or_404(models.TVShow, id=id)
    return render(request, 'shows_list.html',
                  {'show': show})

def add_show(request):
    method = request.method
    if method == 'POST':
        form = forms.ShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.seve()
            return HttpResponse('Show created')
    else:
        form = forms.ShowForm()
    return render(request, 'add_shows.html', {'form': form})

def show_update(request, id):
    show_object = get_object_or_404(models.TVShow, id=id)
    if request.method == 'POST':
        form = forms.ShowForm(instance=show_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Show Updated Successfully')
    else:
        form = forms.ShowForm(instance=show_object)
    return render(request, 'show_update.html', {'object': show_object})

def show_delete(request,id):
    show_object = get_object_or_404(models.TVShow, id=id)
    show_object.delete()
    return HttpResponse('Show Deleted')











