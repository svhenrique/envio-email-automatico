from django.core.exceptions import ValidationError

def validate_email_textarea(container):
    """
    Função usada para validar uma lista de emails
    """
    emails = container.split(',')
    print(emails)
    for e in emails:
        v = e.strip()
        if " " not in v:
            if "@" in v:
                pos = v.index("@")
                if len(v[pos+1:]) > 4 and v[-4:]  == '.com':
                    # len(e[pos+1:]) > 4 para aceitar emails como ex@a.com
                    continue
        raise ValidationError(f'O email "{e}" é invalido.')
    return container


def validate_file_size(arquivo):
    """
    Função usada para validar o tamanho de um arquivo
    """
    if arquivo.size > 30000000:
        raise ValidationError(f'O tamanho máximo é de 30mb.')
    return arquivo




