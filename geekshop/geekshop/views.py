from mainapp.models import Product
from django.views.generic.list import ListView
from django.views.generic import TemplateView


class IndexListView(ListView):
    model = Product
    template_name = "geekshopapp/index.html"

    def get_queryset(self):
        return Product.objects.all()[:4]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "магазин"
        return context


class ContactsListView(TemplateView):
    template_name = "geekshopapp/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "контакты"
        context["locations"] = [
            {
                "city": "Москва",
                "phone": "+7-888-888-8888",
                "email": "info@geekshopapp.ru",
                "address": "В пределах МКАД"
            } for _ in range(3)
        ]
        return context
