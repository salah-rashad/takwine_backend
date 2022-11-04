# from io import BytesIO
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
import pdfkit as pdfkit

# from xhtml2pdf import pisa


def render_to_pdf(template_src: str, css_src: str, data: dict = {}):
    template = get_template(template_src)
    data.update({
        "media_path": settings.MEDIA_ROOT
    })
    html = template.render(data)

    path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path)

    # response = BytesIO()
    # pdf = pisa.pisaDocument(
    #     BytesIO(html.encode("UTF-8",)), response)

    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
        'orientation': 'landscape',
        "enable-local-file-access": None,
    }
    pdf = pdfkit.from_string(
        html, False, options=options, configuration=config, css=css_src)

    if pdf:
        return HttpResponse(pdf, content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)
    return None
