from django.views import generic
from clinic import models
# Контроллеры для model:clinic.models.AppointmentModel.


class AppointmentListView(generic.ListView):
    """Контроллер для получения списка model:clinic.models.AppointmentModel."""

    model = models.AppointmentModel

class AppointmentCreateView(generic.CreateView):
    """Контроллер для создания экземпляра model:clinic.models.AppointmentModel."""

    model = models.AppointmentModel


class AppointmentDetailView(generic.DetailView):
    """Контроллер для получения экземпляра model:clinic.models.AppointmentModel."""

    model = models.AppointmentModel


class AppointmentUpdateView(generic.UpdateView):
    """Контроллер для изменения экземпляра model:clinic.model.AppointmentModel."""
    model = models.AppointmentModel


class AppointmentDeleteView(generic.DeleteView):
    """Контроллер для удаления экземпляра model:clinic.models.AppointmentModel."""

    model = models.AppointmentModel
