from django.shortcuts import render
from . import models


def shows_all(request):
    shows = models.TVShow.objects.all()
    return render(request, 'shows_list.html',
                  {'shows': shows})

def shows_detail(request, id):
    show = get_object_or_404(models.TVShow, id=id)
    return render(request, 'shows_list.html',
                  {'show': show})
