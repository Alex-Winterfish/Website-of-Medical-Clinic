from django.urls import reverse_lazy
from django.views import generic
from clinic import models
from clinic import forms

# Контроллеры для model:clinic.models.AppointmentModel.


class AppointmentListView(generic.ListView):
    """Контроллер для получения списка model:clinic.models.AppointmentModel."""

    model = models.AppointmentModel


class AppointmentCreateView(generic.CreateView):
    """Контроллер для создания экземпляра model:clinic.models.AppointmentModel."""

    template_name = "clinic/appointment_form.html"
    model = models.AppointmentModel
    form_class = forms.AppointmentForm
    success_url = reverse_lazy("clinic:main")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get("pk")
        service_inst = models.MedServiceModel.objects.get(
            id=id
        )  # получаем экземпляр модели медуслуги для передачи в контекст
        service_name = service_inst.name
        context["service_name"] = service_name
        return context

    def form_valid(self, form):
        id = self.kwargs.get("pk")
        service_inst = models.MedServiceModel.objects.get(id=id)
        form.instance.med_serv = service_inst
        form.instance.patient = self.request.user
        return super().form_valid(form)


class AppointmentDetailView(generic.DetailView):
    """Контроллер для получения экземпляра model:clinic.models.AppointmentModel."""

    model = models.AppointmentModel


class AppointmentUpdateView(generic.UpdateView):
    """Контроллер для изменения экземпляра model:clinic.model.AppointmentModel."""

    model = models.AppointmentModel


class AppointmentDeleteView(generic.DeleteView):
    """Контроллер для удаления экземпляра model:clinic.models.AppointmentModel."""

    model = models.AppointmentModel
