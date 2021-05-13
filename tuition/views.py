from django.shortcuts import render
from .models import Contact, Post, Subject
from .froms import ContactForm, PostForm
from django.http.response import HttpResponse
from django.views import View
# Create your views here.
    
class ContactView(View):
    form_class = ContactForm
    template_name = 'contact.html'
    def get(self, request,*args, **kwargs):
        # form ta ke context akare pass koray dite hobe
        form = self.form_class()
        context ={
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid(): 
            form.save()
            return HttpResponse('success')            
        context ={
            'form': form
        }
        return render(request, self.template_name, context)



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

#Subject View
def subview(request):
    sub = Subject.objects.get(name='English')
    post =sub.subject_set.all()
    context ={
        'sub': sub,
        'post': post
    }
    return render(request, 'tuition/subjectview.html', context) 

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