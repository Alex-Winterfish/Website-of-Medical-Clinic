from django.views import generic
from clinic import models

# Контроллеры для model:clinic.models.ResultModel.


class ResultListView(generic.ListView):
    """Контроллер для получения списка объектов model:clinic.models.ResultModel."""

    model = models.ResultModel


class ResultCreateView(generic.CreateView):
    """Контроллер для создания экземпляра model:clinic.models.ResultModel."""

    model = models.ResultModel


class ResultDetailView(generic.DetailView):
    """Контроллер для получения экземпляра model:clinic.models.ResultModel."""

    model = models.ResultModel


class ResultUpdateView(generic.UpdateView):
    """Контроллер для изменеия экземпляра model:clinic.models.ResultModel."""

    model = models.ResultModel


class ResultDeleteView(generic.DeleteView):
    """Контроллер для удаления экземпляа model:clinic.models.ResultModel"""

    model = models.ResultModel
