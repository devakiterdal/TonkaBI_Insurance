from django.shortcuts import render, redirect
from .forms import ClientsForm
from .models import Client
import datetime

from easy_pdf.views import PDFTemplateResponseMixin
from django.views.generic import DetailView
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO
from django.template.loader import render_to_string



def clients_form(request,id=0):
    if request.method == "GET":
        if id ==0:
            form = ClientsForm()
        else:
            client = Client.objects.get(pk=id)
            form = ClientsForm(instance=client)
        return render(request, 'clients/client_form.html',{'form':form})
    else:
        if id == 0:
            form = ClientsForm(request.POST)
        else:
            client = Client.objects.get(pk=id)
            form = ClientsForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
        return redirect('/clients/clients_summary')

def clients_summary(request):
    context = {'summary':Client.objects.all()}
    return render(request, 'clients/client_summary.html',context)

def clients_delete(request,id):
    client = Client.objects.get(pk=id)
    client.delete()
    return redirect('/clients/clients_summary')

def getpdf(request, id):
    client = Client.objects.filter(pk=id)
    html = render_to_string('clients_detail.html', {'client': client,}).encode('utf-8')
    result = BytesIO()
    pdfpage = pisa.pisaDocument(BytesIO(html), result, encoding='UTF-8')
    converted = result.getvalue() if not pdfpage.err else ''

    filename = 'clients_summary.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    response.write(converted)
    return response 