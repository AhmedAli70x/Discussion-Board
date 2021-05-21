from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows':5, 'placeholder':"What's in your mind"}
    ), max_length=2000, help_text='The max lenght of the text is 2000')
    class Meta:
        model = Topic
        fields = ['subject', 'message']