from django.shortcuts import render

def index_function(request):
    return render(request, 'amir/index.html')
