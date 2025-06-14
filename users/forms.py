from django import forms
from users import models
from django.contrib.auth.forms import UserCreationForm


class FeedBackForm(forms.ModelForm):
    """Форма обратной связи model:users.models.FeedBackModel."""

    class Meta:
        model = models.FeedBackModel
        fields = ["theme", "feed_back", "email"]

    def __init__(self, *args, **kwargs):

        super(FeedBackForm, self).__init__(*args, **kwargs)

        self.fields["theme"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Тема вашего отзыва."}
        )
        self.fields["feed_back"].widget.attrs.update(
            {"class": "form-control", "placeholder": "О чем ваш отзыв?"}
        )
        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Укажите ваш email. Мы свяжимся с вами.",
            }
        )


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class CustomUserCreationForm(StyleFormMixin, UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        help_text="Необязательное поле. Введите ваш номер телефона",
    )

    class Meta(models.CustomUser.Meta):
        model = models.CustomUser
        fields = (
            "email",
            "first_name",
            "last_name",
            "patronymic",
            "phone_number",
            "password1",
            "password2",
        )

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер должен состоять только из цифр")
        return phone_number
