from django.urls import reverse_lazy
from django.views import generic
from clinic.models import MedServiceModel

from users.models import FeedBackModel, ContentModel
from users.forms import FeedBackForm
import os
from dotenv import load_dotenv
load_dotenv()


class MainPageView(generic.TemplateView):
    template_name = "clinic/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = ContentModel.objects.get(company=os.getenv('COMPANY_NAME'))
        context["med_services"] = MedServiceModel.objects.all()
        return context


class ContactsView(generic.CreateView):
    template_name = "clinic/contacts.html"
    model = FeedBackModel
    form_class = FeedBackForm
    success_url = reverse_lazy("clinic:main")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = ContentModel.objects.get(company=os.getenv('COMPANY_NAME'))
        return context
