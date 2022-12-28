from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, FormView

from .models import Cards
from .form import GeneratorCardsForm

from uuid import uuid4


class CardsListView(ListView):
    model = Cards
    context_object_name = 'cards'
    paginate_by = 2
     

class CardDetailView(DetailView):
    model = Cards
    context_object_name = 'card'

    def get_object(self, queryset=None):
        card_obj = Cards.objects.filter(pk=self.kwargs['card_number'])[0]
        return card_obj


class GeneratorCardsFormView(FormView):
    form_class = GeneratorCardsForm
    template_name = 'manager_card/generate_cards.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        quantity_cards = int(request.POST['quantity'])
        batch_size = 100    

        if form.is_valid():
            batch = []
            for _ in range(quantity_cards):
                new_obj = Cards(
                    card_series=request.POST['card_series'],
                    card_number=uuid4(),
                    activity_end_date=request.POST['activity_end_date'],
                    amount_on_card=request.POST['amount_on_card'],
                    card_status=True,
                )
                batch.append(new_obj)
            Cards.objects.bulk_create(batch, batch_size=batch_size)
            return redirect('manager_card:cards_list')
        else:
            return self.form_invalid(form)


# ==========================================================================
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import JsonResponse
from .serializers import CardsSerializer


class CardsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer
    lookup_field = 'card_number'
     

    @action(detail=True)
    def relay_status(self, request, *args, **kwargs):
        card = self.get_object()
        if card.card_status:
            card.card_status = False
        else:
            card.card_status = True
        card.save()
        serializer = self.get_serializer(card)
        return JsonResponse({'card_status': serializer.data['card_status']})
        # return JsonResponse(serializer.data)
        # return redirect(request.META.get('HTTP_REFERER'))


    @action(detail=True)
    def delete(self, request, *args, **kwargs):
        card = self.get_object()
        card.delete()
        return redirect(request.META.get('HTTP_REFERER'))