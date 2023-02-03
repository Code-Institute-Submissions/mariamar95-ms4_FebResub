from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was sent. \
                Please allow up to 7 days for a response')
            return redirect('success')
        else:
            messages.error(request, 'Your message was not sent. \
                Please make sure all fields are filled and try again.')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def success(request):
    """ A view to return the success page """
    return render(request, 'contact/success.html')
