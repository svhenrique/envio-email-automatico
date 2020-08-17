from django.shortcuts import render
from django.views.generic import FormView
from .forms import EmailForm
from django.contrib import messages

def index(request):
    form = EmailForm()

    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            form.send_mail()
            messages.success(request, "Email enviado com sucesso.")
            form = EmailForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        "form": form
    }

    return render(request, "index.html", context)

