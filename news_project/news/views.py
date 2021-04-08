from django.views.generic import TemplateView, ListView
from .models import News


class Index(ListView):
    template_name = "news_list.html"

    news = News.objects.all()

    def get_queryset(self):
        return News.objects.order_by('-created_at')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['News'] = self.get_queryset()
        return context
