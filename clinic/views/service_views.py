from django.views import generic
from clinic import models

# Контроллеры для CRUD операций model:clinic.models.MedServiceModel.


class ServiceListView(generic.ListView):
    """Контроллер для вывода списка model:clinic.models.MedServiceModel."""

    model = models.MedServiceModel
    template_name = "clinic/services.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        context["in_group"] = user.groups.filter(name="moders").exists()
        return context


'''class ServiceCreateView(generic.CreateView):
    """Контроллер для создания model:clinic.models.MedServiceModel."""

    model = models.MedServiceModel


class ServiceDetailView(generic.DetailView):
    """Контроллер для получения model:clinic.models.MedServiceModel."""

    model = models.MedServiceModel


class ServiceUpdateView(generic.UpdateView):
    """Контроллер для получения model:clinic.models.MedServiceModel."""

    model = models.MedServiceModel


class ServiceDeleteView(generic.DeleteView):
    """Контроллер для удаления экземпляра model:clinic.models.MedService."""

    model = models.MedServiceModel
'''
