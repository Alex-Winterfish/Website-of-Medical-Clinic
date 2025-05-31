from django.views.generic import TemplateView
from clinic.models import MedServiceModel, MedStaffModel

class MainPageView(TemplateView):
    template_name = 'clinic/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['med_services'] = MedServiceModel.objects.all()
        return context

class CompanyInfo(TemplateView):
    template_name = 'clinic/company_page.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['team'] = MedStaffModel.objects.all()
        return contex
