from io import BytesIO
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context_dict)
    results = BytesIO()
    pdf = pisa.pisaDocument((html.encode("ISO-8859-1")), results) # Uso la funcion pisa le pido que me genere un documento y le paso el parametro para que me tome caracteres en español
                                                                  
    if not pdf.err:
        return HttpResponse(results.getvalue(), content_type = 'application/pdf')
    return None
