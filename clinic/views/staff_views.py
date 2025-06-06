from django.views import generic
from clinic import models
from users.models import ContentModel
import os
from dotenv import load_dotenv

load_dotenv()


# Контроллеры для CRUD операций model:clinic.models.MedStaffModel.
class StaffListView(generic.ListView):
    """Контроллер для вывода списка сущностей models: clinic.model.MedStaffModel."""

    model = models.MedStaffModel
    template_name = "clinic/company_page.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        user = self.request.user
        context["in_group"] = user.groups.filter(name="moders").exists()
        context["company"] = ContentModel.objects.get(company=os.getenv("COMPANY_NAME"))
        return context


'''
class StaffCreateView(generic.CreateView):
    """Контроллер для cсоздания сощности models: clinic.model.MedStaffModel."""

    model = models.MedStaffModel


class StaffUpdateView(generic.UpdateView):
    """Контроллер для изменения сущности models: clinic.model.MedStaffModel."""

    model = models.MedStaffModel


class StaffDetailView(generic.DetailView):
    """Контроллер для получения сущности models: clinic.model.MedStaffModel."""

    model = models.MedStaffModel


class StaffDeleteView(generic.DeleteView):
    """Контроллер для удаления models: clinic.model.MedStaffModel."""

    model = models.MedStaffModel
'''
