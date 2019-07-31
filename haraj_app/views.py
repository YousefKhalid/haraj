from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .form import ContactForm , AddForm, UserForm, ProfileForm, LoginForm
from .models import Add

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User


from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AddSerializer

class AddViewSet(viewsets.ModelViewSet):
    queryset =Add.objects.all()
    serializer_class = AddSerializer

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']    
            email = form.cleaned_data ['email']    
            body = form.cleaned_data ['body']

            send_email(name , email ,body)
            form=ContactForm()
            messages.success(request ,'Thank you for  email us')
            return HttpResponseRedirect(reverse('contact'))

    data = {
        'form': form
        }
    return render (request, 'contact.html', data)

class addUpdate(UpdateView):
    model = Add
    fields = '__all__'
    template_name = 'add_form.html'

class addDelete(DeleteView):
    model = Add
    success_url = reverse_lazy('home')
    template_name = 'add_confirm_delete.html'

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

def detalis(request,pk):
    ad = get_object_or_404(Add, pk=pk)
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


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    messages.error(request, 'user is not active')
            else:
                messages.error(request, 'invalid username of password')
    
    data = {'form': form}
    return render(request, 'login.html', data)

    def send_email(name, email, body):
        print('email is sending')