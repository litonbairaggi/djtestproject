from django.shortcuts import render
from .models import Contact, Post
from .froms import ContactForm
# Create your views here.
    
def contact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid(): 
            form.save()
    else:
        form = ContactForm()    
    return render(request, 'contact.html', {'form': form})

def postview(request):
    post = Post.objects.all()
    context ={
        'post': post
    }
    return render(request, 'tuition/postview.html', context)     