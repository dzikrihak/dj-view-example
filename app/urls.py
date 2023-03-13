from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView, TemplateView

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    # cbv - TemplateView with urls to the point
    # path(
    #     "about/",
    #     TemplateView.as_view(
    #         template_name="about.html", extra_context={"header": "About"}
    #     ),
    # ),
    path("about/", views.AboutView.as_view(), name="about"),
    # path(
    #     "redirect/",
    #     RedirectView.as_view(url="https://www.google.com/?client=safari"),
    #     name="redirect-to-google",
    # ),
    path("redirect/", views.RedirectView.as_view(), name="redirect"),
    path("<int:pk>/", views.PlayerDetailView.as_view(), name="detail"),
    path("lists/", views.PlayerListView.as_view(), name="player-list"),
]
