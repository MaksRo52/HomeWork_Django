from django.forms import ModelForm, forms

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "image", "description", "price", "category"]

    def clean_name(self):
        cleaned_data = self.cleaned_data.get("name")

        if cleaned_data in 'казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар':
            raise forms.ValidationError("Нельзя применять слова из списка : казино, криптовалюта, крипта, биржа, "
                                        "дешево, бесплатно, обман, полиция, радар.")

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get("description")

        if cleaned_data in 'казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар':
            raise forms.ValidationError("Нельзя применять слова из списка : казино, криптовалюта, крипта, биржа, "
                                        "дешево, бесплатно, обман, полиция, радар.")

        return cleaned_data
