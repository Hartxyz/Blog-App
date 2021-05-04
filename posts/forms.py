from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'comment',)

        widgets = {
                'body': forms.Textarea(attrs={'class':'form-control'})
                }