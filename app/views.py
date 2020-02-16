from django.shortcuts import render

from .forms import ContactForm
from .models import Contact




def front(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        form = ContactForm()
    return render(request,"front.html",{'form':form})


