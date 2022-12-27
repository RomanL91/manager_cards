from django.forms import ModelForm
from django import forms

from .models import Cards


class GeneratorCardsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GeneratorCardsForm, self).__init__(*args, **kwargs)
        
        self.fields["quantity"] = forms.IntegerField(
            min_value=1,
            max_value=1000_000,
            # step_size=10
            label='количество'
        )

    class Meta:
        model = Cards
        fields = [
            'card_series',
            'activity_end_date',
            'amount_on_card',
            'card_status'
        ]