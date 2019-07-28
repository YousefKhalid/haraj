from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .form import ContactForm , AddForm
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
 
def send_email(name, email, body):
    print(name, email, body)