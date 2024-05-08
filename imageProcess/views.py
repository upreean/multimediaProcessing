from django.shortcuts import render
from .form import ImageForm
from .models import ImageModel

# Create your views here.
def index(request):
    imgform = ImageForm()
    context = { 
        'title': 'Edited.id',
        'page': 'Image Processing',
        'image_form': imgform,
        'nav': [
            ['/','Home'],
            ['/imageProcess/','Image'],
            ['/audioProcess/','Audio'],
        ],
    }    
    if request.method == 'POST':
        img = ImageModel()
        if len(request.FILES) != 0:
            img.imageFile = request.FILES['imageFile']
            img.save()
            context['imageFile'] = img.imageFile.url
    else: 
        print('ini adalah method get')
    return render(request, 'imageProcess/index.html', context)
