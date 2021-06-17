from django import forms
from blog_app.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author','title','text')
    
        #Adding widget
        widget = {
            'title' : forms.TextInput(attrs = {'class':'textinputclass'}),
            'text': forms.Textarea(attrs = {'class':'editable medium-editor-textarea postcontent'}) #classes used here will be defined in css and some of them in bootstrap
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text')

        widget = {
            'author' : forms.TextInput(attrs = {'class':'textinputclass'}),
            'text': forms.Textarea(attrs = {'class':'editable medium-editor-textarea'}) #classes used here will be defined in bootstrap
        }