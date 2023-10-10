from django.http import HttpResponse
from django.template import loader
from .models import Livro    # adicione esta importação
from .models import TCC    # adicione esta importação

def principal(request):
    template = loader.get_template('principal.html')
    return HttpResponse(template.render())

def livros(request):         # atualize esta função
    livros = Livro.objects.all().values()
    template = loader.get_template('livros.html')
    context = {
        'livros': livros,
    }
    return HttpResponse(template.render(context, request))

def tccs(request):         # atualize esta função
    tccs = TCC.objects.all().values()
    template = loader.get_template('tccs.html')
    context = {
        'tccs': tccs,
    }
    return HttpResponse(template.render(context, request))
def tcc_detalhes(request, id):
    tcc = TCC.objects.get(id=id)
    template = loader.get_template('tcc_detalhes.html')
    context = {
        'tcc': tcc,
    }
    return HttpResponse(template.render(context, request))
def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())