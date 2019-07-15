from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    class Meta:
        model = Topic
        fields = ['text']


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={'cols': 80, 'autofocus': True, 'class': 'form-control'})}

