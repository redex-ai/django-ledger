# Generated by Django 4.2.1 on 2023-08-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ledger', '0008_closingentrymodel_closingentrymodel_unique_ce_all_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entitymodel',
            name='last_closing_date',
            field=models.DateField(blank=True, null=True, verbose_name='Last Closing Entry Date'),
        ),
    ]
