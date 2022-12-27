from django.urls import path

from .views import (
    CardsListView, 
    CardDetailView, 
    CardsViewset, 
    GeneratorCardsFormView
    )


urlpatterns = [
    path('', CardsListView.as_view(), name='cards_list'),
    path('card/<slug:card_number>/', CardDetailView.as_view(), name='card_detail'),
    path('card/<slug:card_number>/relay_status', CardsViewset.as_view({'get': 'relay_status'}), name='relay_status'),
    path('card/<slug:card_number>/delete', CardsViewset.as_view({'get': 'delete'}), name='delete'),
    path('generate_cards/', GeneratorCardsFormView.as_view(), name='generate_cards'),
]