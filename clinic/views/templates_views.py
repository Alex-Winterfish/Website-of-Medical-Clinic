from django.views import generic
from clinic.models import MedServiceModel

class MainPageView(generic.TemplateView):
    template_name = 'clinic/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['med_services'] = MedServiceModel.objects.all()
        return context

class ContactsView(generic.TemplateView):
    template_name = 'clinic/contacts.html'