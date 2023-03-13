from django.contrib.admin.options import RedirectView
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic.list import ListView

from .forms import PlayerForm
from .models import Player


# fbv
def home(request):
    form = PlayerForm()
    players = Player.objects.all()
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form, "players": players}
    return render(request, "./templates/home.html", context)


# cbv - TemplateView with view perspektif


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Header About"
        return context


class PreRedirectView(RedirectView):
    pattern_name = "home:about"

    def get_redirect_url(self, *args, **kwargs):
        print("Customize here")
        return super().get_redirect_url(*args, **kwargs)


class PlayerDetailView(DetailView):
    template_name = "detail.html"
    # queryset = Player.object.all()

    def get_object(self):
        idx = self.kwargs.get("pk")
        return get_object_or_404(Player, id=idx)


class PlayerListView(ListView):
    model = Player
    template_name = "lists.html"
    context_object_name = "Players"
    paginate_by = 1

    def get_queryset(self):
        queryset = Player.objects.filter(first_name="Lionel")
        # queryset = Player.objects.filter(nationality=self.kwargs.get("nationality"))
        return queryset


class AddView(FormView):
    template_name = "add_player.html"
    form_class = PlayerForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
