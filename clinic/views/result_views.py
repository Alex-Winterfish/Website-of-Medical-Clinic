from django.urls import reverse_lazy
from django.views import generic
from clinic import models, forms
from django.utils.timezone import datetime


# Контроллеры для model:clinic.models.ResultModel.


class ResultListView(generic.ListView):
    """Контроллер для получения списка объектов model:clinic.models.ResultModel."""

    template_name = "clinic/moder_page.html"
    form_class = forms.ResultForm
    model = models.ResultModel
    success_url = reverse_lazy("clinic:result_created")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["in_group"] = user.groups.filter(name="moders").exists()
        if models.AppointmentModel.objects.filter(resultmodel__isnull=True).exists():
            context["appointment"] = models.AppointmentModel.objects.filter(
                resultmodel__isnull=True
            )
        else:
            context["app_false"] = (
                True  # передаем в контекст, если процедуры для оформления не существуют
            )

        if models.AppointmentModel.objects.filter(resultmodel__isnull=False).exists():
            context["appointment_done"] = models.AppointmentModel.objects.filter(
                resultmodel__isnull=False
            )

        else:
            context["app_done_false"] = (
                True  # передаем в контекст, если оформленные процедуры не существуют
            )
        return context


class ResultCreateView(generic.CreateView):
    """Контроллер для создания экземпляра model:clinic.models.ResultModel."""

    template_name = "clinic/result_form.html"

    form_class = forms.ResultForm
    model = models.ResultModel
    success_url = reverse_lazy("results:results")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["in_group"] = user.groups.filter(name="moders").exists()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        app_pk = self.kwargs.get(
            "pk"
        )  # pk экземпляра model:clinic.models.AppointmentModel
        if (
            app_pk
        ):  # передаем в форму pk экземпляра model:clinic.models.AppointmentModel
            kwargs["initial"] = kwargs.get("initial", {})
            kwargs["initial"]["appointment"] = app_pk
        return kwargs

    def form_valid(self, form):
        app_pk = self.kwargs.get(
            "pk"
        )  # pk экземпляра model:clinic.models.AppointmentModel
        user_pk = models.AppointmentModel.objects.get(id=app_pk).patient
        form.instance.patient = user_pk
        form.instance.result_date = datetime.now()
        return super().form_valid(form)


class ResultDetailView(generic.DetailView):
    """Контроллер для получения экземпляра model:clinic.models.ResultModel."""

    template_name = "clinic/result.html"
    model = models.ResultModel


'''class ResultUpdateView(generic.UpdateView):
    """Контроллер для изменеия экземпляра model:clinic.models.ResultModel."""

    model = models.ResultModel


class ResultDeleteView(generic.DeleteView):
    """Контроллер для удаления экземпляа model:clinic.models.ResultModel"""

    model = models.ResultModel'''
