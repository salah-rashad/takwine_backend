# from io import BytesIO
import os

import pdfkit as pdfkit
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from rest_framework import status


def render_to_pdf(template_src: str, css_src=None, data: dict = {}):
    template = get_template(template_src)
    data.update({
        "media_path": settings.MEDIA_ROOT,
        "static_path": settings.STATIC_ROOT,
    })
    html = template.render(data)

    # servicePath = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    servicePath = r'/usr/bin/wkhtmltopdf'
    config = pdfkit.configuration(wkhtmltopdf=servicePath)

    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'orientation': 'landscape',
        'enable-local-file-access': None,
    }
    pdf = pdfkit.from_string(
        html, False, options=options, configuration=config, css=css_src)

    if pdf:
        return HttpResponse(pdf, content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=status.HTTP_400_BAD_REQUEST)
