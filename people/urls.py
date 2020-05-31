from django.urls import path

from .views import people_views as pv

urlpatterns = [
    # /people/
    path('', pv.home, name="index"),

    # /people/listar
    path('listar/', pv.listar, name="listar"),

    # /people/detalhar/1
    path('detalhar/<int:id_pessoa>/', pv.detalhar, name="detalhar"),

    # /people/excluir/1
    path('excluir/<int:id_pessoa>/', pv.excluir, name="excluir"),

    path('cadastro/', pv.cadastro, name="cadastro"),
    path('cadastrar/', pv.cadastrar, name="cadastrar"),

    path('edicao/<int:id_pessoa>/', pv.edicao, name="edicao"),
    path('editar/<int:id_pessoa>/', pv.editar, name="editar")
]