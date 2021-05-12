from django.shortcuts import render
from .models import Contact, Post
from .froms import ContactForm, PostForm
from django.http.response import HttpResponse
# Create your views here.
    
def contact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid(): 
            form.save()
    else:
        form = ContactForm()    
    return render(request, 'contact.html', {'form': form})

#post View
def postview(request):
    post = Post.objects.all()
    context ={
        'post': post
    }
    return render(request, 'tuition/postview.html', context) 

#Post Create
def postcreate(request):
    if request.method=="POST":
        #request.FILES use of image file for include
        form =PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save() 
        #MenyToMeny reletionship
        sub = form.cleaned_data['subject']
        for i in sub:
            obj.subject.add(i)
            obj.save()

        class_in = form.cleaned_data['class_in']  
        for i in class_in:
            obj.class_in.add(i)
            obj.save()
        #Used for Message 
        return HttpResponse("Successfully save")    

    else:
        form = PostForm()
        context = {
            'form': form
        }
    return render(request, 'tuition/postcreate.html', context)                   