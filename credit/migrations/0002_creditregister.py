# Generated by Django 4.2.4 on 2023-08-19 04:30
import pandas as pd
from django.db import migrations, models
import django.db.models.deletion
from credit.models import CreditRegister as CreditRegisterClass


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0001_initial'),
    ]

    def insert_init_data(apps, shcema_editor):
        df = pd.read_csv('credit/migrations/data.csv')
        Bank = apps.get_model('credit', 'Bank')
        CreditRegister = apps.get_model('credit', 'CreditRegister')
        for bank in Bank.objects.values_list("id","name"):
            df.loc[df['institucion']==bank[1],'bank_id'] = bank[0]
        for currency in CreditRegisterClass.currency_choices:
            df.loc[df['moneda']==currency[1],'moneda'] = currency[0]
        for status in CreditRegisterClass.credit_status_choices:
            df.loc[df['situacion_credito']==status[1],'situacion_credito'] = status[0]
        list_credit_register_objs = []
        for i, row in df.iterrows():
            list_credit_register_objs.append(
                CreditRegister(
                    currency=row['moneda'],
                    credit_status=row['situacion_credito'],
                    total=row['responsabilidad_total'],
                    bank_id=row['bank_id']
                )
            )
        CreditRegister.objects.bulk_create(list_credit_register_objs)

    def undo_insert_data(apps, shcema_editor):
        CreditRegister = apps.get_model('credit', 'CreditRegister')
        CreditRegister.objects.all().delete()

    operations = [
        migrations.CreateModel(
            name='CreditRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.PositiveSmallIntegerField(choices=[(1, 'Moneda extranjera'), (2, 'Moneda nacional'), (3, 'UDIS')], default=2)),
                ('credit_status', models.PositiveSmallIntegerField(choices=[(1, 'Vencido'), (2, 'Vigente')], default=2)),
                ('total', models.FloatField(default=0.0)),
                ('date', models.DateField(auto_now_add=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credit.bank')),
            ],
        ),
        migrations.RunPython(insert_init_data,reverse_code=undo_insert_data)
    ]
