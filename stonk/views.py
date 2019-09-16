from django.views.generic.base import TemplateView

from stonk.models import Meme


class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['memes'] = Meme.objects.all()
        return kwargs


class DetailView(TemplateView):
    template_name = "home/detail.html"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['meme'] = Meme.objects.get(id=kwargs['id'])
        return kwargs


home = HomeView.as_view()
detail = DetailView.as_view()
