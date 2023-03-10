# Generated by Django 4.1.4 on 2022-12-27 10:35

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('card_series', models.SlugField(help_text='укажите серию карт, например: "подарочные на открытие "', max_length=75, verbose_name='серия карты')),
                ('card_number', models.UUIDField(default=uuid.UUID('eb515c6c-2dc1-4501-8578-07f02b563838'), editable=False, primary_key=True, serialize=False, verbose_name='номер карты')),
                ('date_of_issue', models.DateTimeField(auto_now_add=True, verbose_name='дата/время создания')),
                ('activity_end_date', models.DateTimeField(choices=[(datetime.datetime(2023, 1, 27, 10, 35, 50, 803515), 'One Mouth'), (datetime.datetime(2023, 6, 27, 10, 35, 50, 803563), 'Six Mouth'), (datetime.datetime(2023, 12, 27, 10, 35, 50, 803582), 'One Year')], help_text='выбирете срок годности карты', verbose_name='срок годности')),
                ('date_of_use', models.JSONField(default={'datatime': ['val_1', 'val_2']}, help_text='представление об использовании карты', verbose_name='дата использования')),
                ('amount_on_card', models.DecimalField(decimal_places=2, help_text='укажите остаток баллов/очков/бонусов/и т.д.', max_digits=7, verbose_name='остаток карты')),
                ('card_status', models.BooleanField(default=True, help_text='установите статус карты (активна/не активна)', verbose_name='активна')),
            ],
        ),
        migrations.AddConstraint(
            model_name='cards',
            constraint=models.CheckConstraint(check=models.Q(('amount_on_card__gte', 0), ('amount_on_card__lte', 100000)), name='manager_card_cards_amount_on_card'),
        ),
    ]
