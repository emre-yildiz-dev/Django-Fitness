from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from .models import Message


def message_post(request):
    # my_form = ContactForm()
    if request.method == "POST":
        # my_form = ContactForm(request.POST)
        # if my_form.is_valid():
        message = Message()
        message.name = request.POST.get('name')
        message.phone = request.POST.get('phone')
        message.message = request.POST.get('message')
        message.email = request.POST.get('email')
        message.subject = request.POST.get('subject')
        x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forw_for is not None:
            message.ipaddress = x_forw_for.split(',')[0]
        else:
            message.ipaddress = request.META.get('REMOTE_ADDR')
        print(request.POST)
        message.save()
        return render(request, 'contact-us.html')
    else:
        messages.error(request, 'Invalid form submission.')
        messages.error(request, form.errors)
    # else:
    #     form = ContactForm()
    # context = {
    #     "form": my_form
    # }
    return render(request, "message-post")
