from django import forms
from decouple import config
from django.core.mail.message import EmailMessage
from .validators import validate_email_textarea, validate_file_size

print(config('EMAIL'))
print(config('PASSWORD'))
class EmailForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=150)
    assunto = forms.CharField(label='Assunto', max_length=100)
    emails = forms.CharField(label='E-mails', widget=forms.Textarea(), validators=[validate_email_textarea])
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
    arquivo = forms.FileField(label='Arquivo', max_length=50, validators=[validate_file_size])

    def send_mail(self):
        nome = self.cleaned_data['nome']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        emails = self.cleaned_data['emails']
        arquivo = self.cleaned_data['arquivo']

        # Complete as informações
        mail = EmailMessage(
            subject = f'E-mail enviado pelo sistema Django - {assunto}',
            body = f"{mensagem}\nBy: {nome}",
            from_email = config('EMAIL'),
            to = [e for e in emails.strip().split(',')],
        )

        mail.attach(arquivo.name, arquivo.read(), arquivo.content_type)
        mail.send()










