from django import forms
from .models import Contact, Post


class ContactForm(forms.ModelForm):
    # It's use for only one 1 object/ field
    # name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'}), label='Your name')
    class Meta:
        model=Contact 
        fields ='__all__'
    # initials value included for forms    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label='My name'
        self.fields['name'].initial='My name is '
        self.fields['phone'].initial='+8801'
        self.fields['content'].initial='My problem is'

    def clean_name(self):
        value=self.cleaned_data.get('name')
        num_of_w=value.split(' ')
        if len(num_of_w) > 4:
            self.add_error('name', 'Name can have maximum of 4 words')    
        else:
            return value
            

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'}),
            'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your phone'}),
            'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Say somthing', 'rows':8})
        }
        labels={
            'name':'Your name',  
            'phone':'Your phone',
            'content':'Your words'
        }


class ContactFormtwo(forms.ModelForm):
    class Meta:
        model=Contact 
        fields ='__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model=Post 
        #fields ='__all__'
        exclude = ['user','created_at', 'slug']
        widgets={
            'class_in': forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
            }),
            'subject': forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
            })
        }