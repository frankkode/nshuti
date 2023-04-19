from django import forms
from .models import Blog



class ContactForm(forms.Form):
    name = forms.CharField( max_length=100)
    subject = forms.CharField( max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'content']
       
