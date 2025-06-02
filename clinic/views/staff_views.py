from django.views import generic
from clinic import models


# Контроллеры для CRUD операций model:clinic.models.MedStaffModel.
class StaffListView(generic.ListView):
    """Контроллер для вывода списка сущностей models: clinic.model.MedStaffModel."""

    model = models.MedStaffModel
    template_name = "clinic/company_page.html"


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
