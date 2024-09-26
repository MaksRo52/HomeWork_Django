from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version, Category


class StyleFormMixin(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ["name", "image", "description", "price", "category"]

    def clean_name(self):
        cleaned_data = self.cleaned_data.get("name")
        words = cleaned_data.split(" ")
        for word in words:
            if word in [
                "казино",
                "криптовалюта",
                "крипта",
                "биржа",
                "дешево",
                "бесплатно",
                "обман",
                "полиция",
                "радар",
            ]:
                raise forms.ValidationError(
                    "Нельзя применять слова из списка : казино, криптовалюта, крипта, биржа, "
                    "дешево, бесплатно, обман, полиция, радар."
                )

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get("description")
        words = cleaned_data.split(" ")
        for word in words:
            if word in [
                "казино",
                "криптовалюта",
                "крипта",
                "биржа",
                "дешево",
                "бесплатно",
                "обман",
                "полиция",
                "радар",
            ]:
                raise forms.ValidationError(
                    "Нельзя применять слова из списка : казино, криптовалюта, крипта, биржа, "
                    "дешево, бесплатно, обман, полиция, радар."
                )

        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"

    def clean_active(self):
        cleaned_data = self.cleaned_data.get("active")

        if cleaned_data and not self.instance.product and "active" > 1:
            raise forms.ValidationError("Версия должна привязана к продукту.")

        return cleaned_data


class CategoryForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
