from django.shortcuts import render
from .models import Contact, Post, Subject
from .froms import ContactForm, PostForm
from django.http.response import HttpResponse
from django.views import View
from django.views.generic import FormView, CreateView, ListView
from django.urls import reverse_lazy


# Create your views here.
    

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'    
    #success_url='/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


    def form_invalid(self, form):
        #ja khush ta likte pari ekhane

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('contact')  #  'contact' eta holo ami kon view te jete chasci sei view er name  


# Create Class basde View  
  
# class ContactView(View):
#     form_class = ContactForm
#     template_name = 'contact.html'
#     def get(self, request,*args, **kwargs):
#         # form ta ke context akare pass koray dite hobe
#         form = self.form_class()
#         context ={
#             'form': form
#         }
#         return render(request, self.template_name, context)

#     def post(self, request,*args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid(): 
#             form.save()
#             return HttpResponse('success')            
#         context ={
#             'form': form
#         }
#         return render(request, self.template_name, context)




# create function based View
def contact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid(): 
            form.save()
    else:
        form = ContactForm()    
    return render(request, 'contact.html', {'form': form})

class PostListView(ListView):
    #model = Post 
    queryset = Post.objects.filter(user=2)
    template_name = 'tuition/postlist.html'
    context_object_name = 'posts'
    #extra context pass korte hoy e vabe
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["posts"] = context.get('object_list') 
        context["mess"] = 'This is post list'
        return context
    

#post View function besed
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


#Post Create Class based View (it's better)
class PostCreateView(CreateView):
    model = Post 
    form_class = PostForm
    template_name = 'tuition/postcreate.html'
    #success_url = '/'
    def form_invalid(self, form):
        form.instance.user = self.request.user    
        return super().form_valid(form)     
    def get_success_url(self):  # if success
        #id = self.object.id  
        return reverse_lazy('tuition:subjects')   # tuition= appName & subjects = url path


#Post Create function based view (It's not use)
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