from django.contrib.auth.models import User
from django.views.generic import DetailView

class ProfileDetailView(DetailView):
    http_method_names = ["get"]
    template_name = 'profiles/detail.html'
    model = User
    context_object_name = "user"
    slug_field = "username" #context on how to get profile
    slug_url_kwarg = "username"