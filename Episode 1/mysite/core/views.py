from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'core/index.html', {'title': 'TailwindCSS4 dengan Django5'})
