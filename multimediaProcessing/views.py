from django.shortcuts import render

def index(request):
    context = {
        'title': 'Edited.id',
        'page': 'Home',
        'nav': [
            ['/','Home'],
            ['/imageProcess/','Image'],
            ['/audioProcess/','Audio'],
        ],
    }    
    return render(request, "index.html", context)