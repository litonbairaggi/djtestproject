from django.shortcuts import render
from .models import Contact, Post, Subject, Class_in
from .froms import ContactForm, PostForm
from django.http.response import HttpResponse
from django.views import View
from django.views.generic import FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

# function based method is Searching
def search(request):
    query =request.POST.get('search', '')
    if query:
        queryset =(Q(title__icontains=query)) | (Q(details__icontains=query)) | (Q(medium__icontains=query)) | (Q(category__icontains=query)) | (Q(subject__name__icontains=query)) | (Q(class_in__name__icontains=query))
        results =Post.objects.filter(queryset).distinct() 
    else:
        results =[]
    context={
        'results': results
    }        
    return render(request, 'tuition/search.html', context)

def filter(request):
    if request.method=="POST":
        subject= request.POST['subject']   
        class_in= request.POST['class_in']  
        salary_from= request.POST['salary_from']  
        salary_to= request.POST['salary_to']  
        available= request.POST['available']  
        if subject or class_in:
            queryset =(Q(subject__name__icontains=subject)) & (Q(class_in__name__icontains=class_in)) 
            results =Post.objects.filter(queryset).distinct() 
            if available:
                results=results.filter(available=True)
            if salary_from:
                results = results.filter(salary__gte=salary_from)    
            if salary_to:
                results = results.filter(salary__lte=salary_to)    
        else:
            results =[]  

        context={
        'results': results
        }        
        return render(request, 'tuition/search.html', context)   


# Create your views here.
class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'    
    #success_url='/'
    def form_valid(self, form):
        form.save()
        messages.info(self.request, 'Form successfully submitted!')
        return super().form_valid(form)

    def form_invalid(self, form):
        #ja khush ta likte pari ekhane
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('homeview')  #  'contact' eta holo ami kon view te jete chasci sei view er name  


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
    initials={
        'name':'My name is',
        'phone':'+8801',
        'content':'My problem is'
    }
    if request.method=="POST":
        form = ContactForm(request.POST, initial=initials)
        if form.is_valid(): 
            form.save()
    else:
        form = ContactForm(initial=initials)    
    return render(request, 'contact.html', {'form': form})

class PostListView(ListView):
    #model = Post 
    #queryset = Post.objects.filter(user=1)
    queryset = Post.objects.all()
    template_name = 'tuition/postlist.html'
    context_object_name = 'posts'
    #extra context pass korte hoy e vabe
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["posts"] = context.get('object_list') 
        # context["mess"] = 'This is post list'
        context['subjects']= Subject.objects.all()
        context['classes']= Class_in.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post 
    template_name = 'tuition/postdetail.html'
    #extra context pass korte hoy e vabe
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["posts"] = context.get('object') 
        context["mess"] = 'This is post detail view'
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

#Post Update Class based View
class PostEditView(UpdateView):
    model = Post 
    form_class = PostForm
    template_name = 'tuition/postcreate.html'    
    def get_success_url(self):  # if success
        id = self.object.id  
        return reverse_lazy('tuition:postdetail', kwargs={'pk': id})

class PostDeleteView(DeleteView):
    model = Post 
    template_name = 'tuition/delete.html' 
    success_url = reverse_lazy('tuition:postlist')       


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