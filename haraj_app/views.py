from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseRedirect, Http404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .form import ContactForm , AddForm, UserForm, ProfileForm, LoginForm
from .models import Add

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']    
            email = form.cleaned_data ['email']    
            body = form.cleaned_data ['body']

            send_email(name , email ,body)
            messages.success(request ,'Thank you for  email us')
            return HttpResponseRedirect('/contact/')

    data = {
        'form': form
        }
    return render (request, 'contact.html', data)

def index(request):
    adds = Add.objects.all()
    data = {    
        'adds': adds
    }
    return render(request, 'index.html',data)
 
 
def add(request):
    form = AddForm()
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    data={    
         'form':form
     }

    return render(request, 'add.html', data)

def detalis(requset,pk):
    ad = get_object_or_404(Add,pk=pk)
    data = {    
        'ad' : ad
    }
    return render(request, 'detalis.html' , data)


def register(request):
    userForm = UserForm()
    profileForm = ProfileForm()
    
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        profileForm = ProfileForm(request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse('home'))

    data = { 'userForm': userForm, 'profileForm': profileForm}
    return render(request, 'register.html', data)

