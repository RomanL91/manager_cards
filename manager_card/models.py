from django.db import models

from dateutil.relativedelta import relativedelta

from uuid import uuid4
import datetime


class MMM(models.Choices):
    one_mouth = datetime.datetime.now() + relativedelta(months=+1)
    six_mouth = datetime.datetime.now() + relativedelta(months=+6)
    one_year = datetime.datetime.now() + relativedelta(months=+12)


class Cards(models.Model):
    #  может поправить?
    card_series = models.SlugField(
        max_length=75,
        help_text='укажите серию карт, например: "подарочные на открытие "',
        verbose_name='серия карты'
    )
    card_number = models.UUIDField(
        primary_key=True,
        default=uuid4(),
        editable=False,
        verbose_name='номер карты'
    )
    date_of_issue = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        verbose_name='дата/время создания'
    )
    activity_end_date = models.DateTimeField(
        choices=MMM.choices,
        help_text='выбирете срок годности карты',
        verbose_name='срок годности'
    )
    date_of_use = models.JSONField(
        help_text='представление об использовании карты',
        verbose_name='дата использования',
        default={'datatime': ['val_1', 'val_2']}
    )
    amount_on_card = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        help_text='укажите остаток баллов/очков/бонусов/и т.д.',
        verbose_name='остаток карты'
    )
    card_status = models.BooleanField(
        default=True,
        help_text='установите статус карты (активна/не активна)',
        verbose_name='активна',
        blank=False,
    )

    class Meta:
        constraints = (
            models.CheckConstraint(
                check=models.Q(amount_on_card__gte=0) & \
                    models.Q(amount_on_card__lte=100_000),
                    name='%(app_label)s_%(class)s_amount_on_card'
            ),
        )