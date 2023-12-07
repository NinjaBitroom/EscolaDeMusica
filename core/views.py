from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from core.models import Musico


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class MusicosView(ListView):
    template_name = 'musicos.html'
    model = Musico
    context_object_name = 'musicos'


class MusicosCreateView(CreateView):
    template_name = 'formmusico.html'
    model = Musico
    success_url = reverse_lazy('musicos')
    fields = ['nome', 'nacionalidade', 'nascimento']


class MusicosUpdateView(UpdateView):
    template_name = 'formmusico.html'
    model = Musico
    success_url = reverse_lazy('musicos')
    fields = ['nome', 'nacionalidade', 'nascimento']


class MusicosDeleteView(DeleteView):
    template_name = 'excluirmusico.html'
    model = Musico
    success_url = reverse_lazy('musicos')
