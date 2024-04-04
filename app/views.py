from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import ImageUploadForm
from django.http import JsonResponse
from django.http import HttpResponse
from . models import CroppedImage


def hello_world(request):
    return HttpResponse("Hello, world!")


def upload_and_crop(request):
    form = ImageUploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'works'})
    context = {'form': form}
    return render(request, 'crop.html', context)


def upload(request):
    if request.method=='POST':
        file = request.FILES['file']
        data=CroppedImage()
        data.file=file
        data.save()

    return render(request,"crop2.html")