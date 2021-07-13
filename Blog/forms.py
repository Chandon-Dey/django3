from django import  forms
from .models import Comment

class CommentForm():
    class Meta:
        model= Comment
        fields=('name','body')