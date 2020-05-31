from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.shortcuts import render
from datetime import datetime

from ..models import Pessoa, Endereco, Escolaridade, Trabalho

@require_http_methods(["GET"])
def home(request):
    return render(request, 'index.html', {})

@csrf_exempt
def listar(request):
    if(request.method=="POST"):
        raise Exception("Requisições POST não são permitidas")
    else:
        result = Pessoa.objects.all()
        template = loader.get_template('listar.html')
        context = {
            'lista' : result,
        }
        return HttpResponse(template.render(context, request))

def detalhar(request, id_pessoa):
    
    try:
        pessoa = Pessoa.objects.get(id=id_pessoa)
        print(f"""Detalhar pessoa de ID = {id_pessoa}""")
        resultEndereco = Endereco.objects.filter(pessoa__id=id_pessoa)

        endereco = 'null'
        if(resultEndereco):
            endereco = resultEndereco[0]

        resultEscolaridade = Escolaridade.objects.filter(pessoa__id=id_pessoa)

        escolaridade = 'null'
        if(resultEscolaridade):
            escolaridade = resultEscolaridade[0]

        resultTrabalho = Trabalho.objects.filter(pessoa__id=id_pessoa)

        trabalho = 'null'
        if(resultTrabalho):
            trabalho = resultTrabalho[0]

        context = {'pessoa':pessoa, 
                   'endereco':endereco,
                   'escolaridade':escolaridade,
                    'trabalho':trabalho}
    except ObjectDoesNotExist:
        context = {'id':id_pessoa}

    return render(request, 'detalhe.html', context)

def cadastro(request):
    template = loader.get_template('cadastrar.html')
    
    context = { 
        'sexo' : [],
        'ufs' : [],
        'niveis' : [],
        'progressos' : []
    }

    fieldsGender = Pessoa.GENDER_CHOICES
    for field, value in fieldsGender:
        itemGender = {"key" : field, "value" : value}
        context["sexo"].append(itemGender)

    fieldsUf = Endereco.UF_CHOICES
    for uf, estado in fieldsUf:
        itemUf = {"key" : uf, "value" : estado}
        context["ufs"].append(itemUf)

    fieldsEscolaridade = Escolaridade.SCHOLARITY_CHOICES
    for field, value in fieldsEscolaridade:
        itemEscolaridade = {"key" : field, "value" : value}
        context["niveis"].append(itemEscolaridade)

    fieldsProgressoEscolaridade = Escolaridade.PROGRESS_CHOICES
    for field, value in fieldsProgressoEscolaridade:
        itemProgresso = {"key" : field, "value" : value}
        context["progressos"].append(itemProgresso)

    #print(f"""context janela = {context}""")

    return HttpResponse(template.render(context, request))

@csrf_exempt
def edicao(request, id_pessoa):
    template = loader.get_template('editar.html')

    try:
        pessoa = Pessoa.objects.get(id=id_pessoa)

        #print(f"""dtNascimento = {pessoa.data_nascimento}""")
        if(pessoa.data_nascimento):
            dtNascimento = '%s-%s-%s' % (pessoa.data_nascimento.strftime("%Y"), pessoa.data_nascimento.strftime("%m"), pessoa.data_nascimento.strftime("%d"))
            pessoa.data_nascimento = dtNascimento
            #print(f"""data_nascimento = {pessoa.data_nascimento}""")

        print(f"""Editar pessoa de ID = {id_pessoa}""")
        resultEndereco = Endereco.objects.filter(pessoa__id=id_pessoa)

        endereco = 'null'
        if(resultEndereco):
            endereco = resultEndereco[0]

        resultEscolaridade = Escolaridade.objects.filter(pessoa__id=id_pessoa)

        escolaridade = 'null'
        if(resultEscolaridade):
            escolaridade = resultEscolaridade[0]

        resultTrabalho = Trabalho.objects.filter(pessoa__id=id_pessoa)

        trabalho = 'null'
        if(resultTrabalho):
            trabalho = resultTrabalho[0]

        context = {'pessoa':pessoa, 
                    'endereco':endereco,
                    'escolaridade':escolaridade,
                    'trabalho':trabalho,
                    'sexo' : [],
                    'ufs' : [],
                    'niveis' : [],
                    'progressos' : []}

        fieldsGender = Pessoa.GENDER_CHOICES
        for field, value in fieldsGender:
            itemGender = {"key" : field, "value" : value}
            context["sexo"].append(itemGender)

        fieldsUf = Endereco.UF_CHOICES
        for uf, estado in fieldsUf:
            itemUf = {"key" : uf, "value" : estado}
            context["ufs"].append(itemUf)

        fieldsEscolaridade = Escolaridade.SCHOLARITY_CHOICES
        for field, value in fieldsEscolaridade:
            itemEscolaridade = {"key" : field, "value" : value}
            context["niveis"].append(itemEscolaridade)

        fieldsProgressoEscolaridade = Escolaridade.PROGRESS_CHOICES
        for field, value in fieldsProgressoEscolaridade:
            itemProgresso = {"key" : field, "value" : value}
            context["progressos"].append(itemProgresso)
            
    except ObjectDoesNotExist:
        context = {'id':id_pessoa}

    return HttpResponse(template.render(context, request))

@require_http_methods(["POST"])
@csrf_exempt
def excluir(request, id_pessoa):
    try:
        pessoa = Pessoa.objects.get(id=id_pessoa)
        pessoa.delete()
        context = {
            'nome' : pessoa.nome,
            'id' : id_pessoa,
        }
    except ObjectDoesNotExist:
        context = {'id':id_pessoa}

    return render(request, 'remocao.html', context)

@require_http_methods(["POST"])
@csrf_exempt
def cadastrar(request):
    #dtNascimento = datetime.strptime(request.POST['dtNascimento'], "%d/%m/%Y").date()
    dtNascimento = request.POST['dtNascimento']
    if(dtNascimento == ""):
        dtNascimento = None
    
    p = Pessoa(nome=request.POST['nome'], 
               idade=request.POST['idade'],
               data_nascimento=dtNascimento,
               cpf=request.POST['cpf'],
               email=request.POST['email'], 
               sexo=request.POST['sexo'])

    end = Endereco(pessoa=p,
                   logradouro=request.POST['logradouro'],
                   numero=request.POST['numero'],
                   bairro=request.POST['bairro'],
                   cep=request.POST['cep'],
                   municipio=request.POST['municipio'],
                   estado=request.POST['estado'])

    anoFinal=request.POST['anoFinal']
    if(anoFinal == ""):
        anoFinal = None

    esc = Escolaridade(pessoa=p,
                       progresso=request.POST['progresso'],
                       nivel=request.POST['nivel'],
                       instituicao=request.POST['instituicao'],
                       anoFinal=anoFinal, 
    )

    temEmprego=request.POST['optradio']
    if(temEmprego == 'True'):
        empresa=request.POST['empresa']
        cargo=request.POST['cargo']
    else:
        empresa=None
        cargo=None
    
    trab = Trabalho(pessoa=p,
                       temEmprego=temEmprego,
                       empresa=empresa,
                       cargo=cargo,
    )

    p.save()
    end.save()
    esc.save()
    trab.save()

    context = {
            'nome' : p.nome,
            'id' : p.id,
    }
    return render(request, 'adicao.html', context)


@require_http_methods(["POST"])
@csrf_exempt
def editar(request, id_pessoa):
    dtNascimento = request.POST['dtNascimento']
    if(dtNascimento == ""):
        dtNascimento = None
    
    p = Pessoa(id=id_pessoa,
               nome=request.POST['nome'], 
               idade=request.POST['idade'],
               data_nascimento=dtNascimento,
               cpf=request.POST['cpf'],
               email=request.POST['email'], 
               sexo=request.POST['sexo'])

    resultEndereco = Endereco.objects.filter(pessoa__id=id_pessoa)
    end = None
    if(resultEndereco):
        endereco = resultEndereco[0]
        end = Endereco(id=endereco.id,
                    pessoa_id=id_pessoa,
                    logradouro=request.POST['logradouro'],
                    numero=request.POST['numero'],
                    bairro=request.POST['bairro'],
                    cep=request.POST['cep'],
                    municipio=request.POST['municipio'],
                    estado=request.POST['estado'])

    resultEscolaridade = Escolaridade.objects.filter(pessoa__id=id_pessoa)
    esc = None
    if(resultEscolaridade):
        escolaridade = resultEscolaridade[0]
        anoFinal=request.POST['anoFinal']
        if(anoFinal == ""):
            anoFinal = None

        esc = Escolaridade(id=escolaridade.id,
                        pessoa_id=id_pessoa,
                        progresso=request.POST['progresso'],
                        nivel=request.POST['nivel'],
                        instituicao=request.POST['instituicao'],
                        anoFinal=anoFinal, 
        )

    resultTrabalho = Trabalho.objects.filter(pessoa__id=id_pessoa)
    trab = None
    if(resultTrabalho):
        trabalho = resultTrabalho[0]
        temEmprego=request.POST['optradio']
        if(temEmprego == 'True'):
            empresa=request.POST['empresa']
            cargo=request.POST['cargo']
        else:
            empresa=None
            cargo=None
    
        trab = Trabalho(id=trabalho.id,
                        pessoa_id=id_pessoa,
                        temEmprego=temEmprego,
                        empresa=empresa,
                        cargo=cargo,
        )

    p.save()
    end.save()
    esc.save()
    trab.save()

    context = {
            'nome' : p.nome,
            'id' : p.id,
    }
    return render(request, 'edicao.html', context)