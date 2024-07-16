from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Object

def object_list(request):
    object_list = Object.objects.all()
    context = {
        'object_list': object_list
    }
    return render(request, 'objects/index.html', context)

def object_detail(request, object_id):
    object = get_object_or_404(Object, pk=object_id)
    context = {
        'object': object
    }
    return render(request, 'objects/detail.html', context)

def new_fucnction(request):
    return HttpResponse('OK')