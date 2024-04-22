from django.forms import BooleanField, ModelForm, forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'picture', 'category', 'price_for_purchase']

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        check_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if set(check_words) & set(self.cleaned_data['name'].lower().split()):
            raise forms.ValidationError('не могут создавать продукты с запрещенными словами в названии')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        check_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if set(check_words) & set(self.cleaned_data['description'].lower().split()):
            raise forms.ValidationError('не могут создавать продукты с запрещенными словами в описании')
        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
