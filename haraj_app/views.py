from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .form import ContactForm , Add
from .models import Add


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
    form = Add()
    if request.method == 'POST':
        form = Add(request.POST)
        form.save(commit=True)
        messages.success(request ,'Your ad have add ')
        return HttpResponseRedirect('/home/')

    data = {    
        'form':form
    }

    return render(request, 'add.html')
 
def send_email(name, email, body):
    print(name, email, body)