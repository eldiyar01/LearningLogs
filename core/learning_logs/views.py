from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def home(request):
    return render(request, 'learning_logs/home.html')


@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, pk):
    topic = get_object_or_404(Topic, id=pk)
    entries = topic.entries.order_by('-date')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def create_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            created_topic = form.save(commit=False)
            created_topic.owner = request.user
            created_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/crud/create_topic.html', context)


def edit_topic(request, pk):
    topic = get_object_or_404(Topic, id=pk)
    if request.method != 'POST':
        form = TopicForm(instance=topic)
    else:
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/crud/edit_topic.html', context)


@login_required
def delete_topic(request, pk):
    topic = get_object_or_404(Topic, id=pk)
    if request.method == 'POST':
        topic.delete()
        return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'topic': topic}
    return render(request, 'learning_logs/crud/delete_topic.html', context)


@login_required
def create_entry(request, pk):
    topic = get_object_or_404(Topic, id=pk)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            created_entry = form.save(commit=False)
            created_entry.topic = topic
            created_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[pk]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/crud/create_entry.html', context)


@login_required
def edit_entry(request, pk):
    entry = get_object_or_404(Entry, id=pk)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/crud/edit_entry.html', context)


@login_required
def delete_entry(request, pk):
    entry = get_object_or_404(Entry, id=pk)
    if request.method == 'POST':
        entry.delete()
        return HttpResponseRedirect(reverse('learning_logs:topic', args=[entry.topic.id]))
    context = {'entry': entry}
    return render(request, 'learning_logs/crud/delete_entry.html', context)
