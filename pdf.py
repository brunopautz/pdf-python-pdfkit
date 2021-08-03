from pdfkit import from_string
from jinja2 import Environment
from jinja2 import FileSystemLoader


'''
    função resposanvel por passar o conteudo para template html
'''
def create_pdf():
    
    '''
        o conteudo dos key podem ser dinamicos
    '''
    template_vars = {
        'title': 'Teste PDF',
        'content': 'Bruno Pautz de Oliveira'
    }

    '''
        busca diretorio COMPLETO onde esta o template
    '''
    env = Environment(loader=FileSystemLoader('/usr/local/bin/w-termocenter-python/pdf/template'))

    '''
        busca o template
    '''
    template = env.get_template('template.html')

    '''
        renderiza o conteudo da variveis
    '''
    html_out = template.render(template_vars)

    '''
        define algumas opções
        é possivel passar o css aqui ou direto no template html
    '''
    arquivo = from_string(
        html_out,
        False,
        options={'page-size': 'Letter',
                 'margin-top': '0.75in',
                 'margin-right': '0.75in',
                 'margin-bottom': '0.75in',
                 'margin-left': '0.75in',
                 'encoding': "UTF-8"}

    )

    return arquivo

'''
    funcao responsvel por salvar o arquivo em pdf
    o nome do arquivo pode ser dinamico
    basta trocar o relatorio.pdf
    pelo nome que desejar
'''
def save_pdf(arquivo):
    with open('/usr/local/bin/w-termocenter-python/pdf/relatorio/relatorio.pdf', 'wb+') as file:
        file.write(arquivo)


pdf_file = create_pdf()
save_pdf(pdf_file)