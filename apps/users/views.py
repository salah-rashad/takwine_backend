import locale
import os

from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse
from django.views import View
from rest_framework import status

from utils.render_to_pdf import render_to_pdf

from .models import Certificate


class CertificateView(View):
    def get(self, request: HttpRequest, pk):
        try:
            download = request.headers.get("download")
        except:
            raise

        cert = Certificate.objects.filter(id=pk).first()

        if cert is not None:
            user_name = cert.user.getFullName() if cert.user is not None else None
            title = cert.course.title if cert.course is not None else None
            locale.setlocale(locale.LC_ALL, 'ar_SA.UTF8')
            date = cert.date.strftime("%A، %d %B %Y")

            data = {
                'user_name': user_name,
                'result': cert.result,
                'course_title': title,
                'issue_date': date
            }

            css = [
                os.path.join(settings.STATIC_ROOT, 'certificate_req', 'css', 'styles.css'),
                os.path.join(settings.STATIC_ROOT, 'certificate_req', 'css', 'bootstrap.min.css'),
            ]

            pdf = render_to_pdf(
                'certificate.html',
                css_src=css,
                data=data
            )

            filename = "certificate_%s.pdf" % (cert.id)

            if download == "true":
                response = HttpResponse(pdf, content_type='application/pdf')
                content = "attachment; filename=%s" % (filename)
            else:
                response = FileResponse(pdf, content_type='application/pdf')
                content = "inline; filename=%s" % (filename)

            response['Content-Disposition'] = content
            return response

        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
