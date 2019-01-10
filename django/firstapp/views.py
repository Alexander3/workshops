from django.contrib.auth.models import User
from django.utils.timezone import now
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        return {
            'time': now().isoformat(),
            'user': User.objects.get(username='admin')
        }
