from rest_framework import serializers
from .models import Cards

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = (
            'card_series',
            'card_number',
            'date_of_issue',
            'activity_end_date',
            'date_of_use',
            'amount_on_card',
            'card_status',
        )