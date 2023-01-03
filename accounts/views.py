from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UserForm
from django.urls import reverse_lazy

# Create your views here.
class UserCreate(CreateView):
    template_name = 'accounts/form.html'
    form_class = UserForm
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title'] = 'Create User'
        context ['bootom'] = 'Register'
        return context