from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import SignUpForm, SignInForm


def signup(request):
    if request.method != 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:home'))
    context = {'form': form}
    return render(request, 'users/signup.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('learning_logs:home'))
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username, password))
                error = ("Wrong username or password")
                return render(request, 'users/sign_in.html', {'form': form, 'error': error})
    else:
        form = SignInForm()
        context = {'form': form}
        return render(request, 'users/sign_in.html', context)


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:home'))
