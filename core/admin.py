from django.contrib import admin

from .models import (Sinfonia, Musico, Funcao, Instrumento, Orquestra,
                     Executa, AptoA, Apresenta, Compoe, Usa)


# Register your models here.
@admin.register(Sinfonia)
class SinfoniaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'compositor', 'data_criacao')


@admin.register(Musico)
class MusicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade', 'nascimento')


@admin.register(Funcao)
class FuncaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modelo')


@admin.register(Orquestra)
class OrquestraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'pais', 'data_criacao')


@admin.register(Executa)
class ExecutaAdmin(admin.ModelAdmin):
    list_display = ('desempenho', 'orquestra', 'sinfonia')


@admin.register(AptoA)
class AptoAAdmin(admin.ModelAdmin):
    list_display = ('musico', 'funcao')


@admin.register(Apresenta)
class ApresentaAdmin(admin.ModelAdmin):
    list_display = ('musico', 'sinfonia')


@admin.register(Compoe)
class CompoeAdmin(admin.ModelAdmin):
    list_display = ('musico', 'orquestra')


@admin.register(Usa)
class UsaAdmin(admin.ModelAdmin):
    list_display = ('funcao', 'instrumento')
