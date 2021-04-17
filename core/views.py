from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # sender = form.cleaned_data['email']
            send_mail(f'{subject} Portfolio Contact', message, 'ashutoshacharya24@gmail.com',
                      ['ashutoshacharya24@gmail.com'],
                      fail_silently=True)
    return render(request, 'home.html')
