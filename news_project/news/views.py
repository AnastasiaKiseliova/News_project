from django.views.generic import ListView
from .models import News, Category


class Index(ListView):
    template_name = "news_list.html"

    news = News.objects.all()

    def get_queryset(self):
        return News.objects.all()

    def get_categories(self):
        return Category.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['News'] = self.get_queryset()
        context['Categories'] = self.get_categories()
        return context
