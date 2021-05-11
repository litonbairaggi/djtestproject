from django.shortcuts import render, HttpResponse


def home(request):
    if request.method=="POST":        
        name = ['A', 'B', 'C', 'D', 'E', 'F']
    else:
        name = []
    context = {
        'name':name,
    }
    return render(request, 'home.html', context)

