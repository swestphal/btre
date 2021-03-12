from django.shortcuts import render

# Create your views here.


def index(request):
    # return HttpResponse('<h1>hello</h1>')
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')
