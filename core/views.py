from django.views.generic import TemplateView, ListView

from core.models import Musico


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class MusicosView(ListView):
    template_name = 'musicos.html'
    model = Musico
    context_object_name = 'musicos'
