# Generated by Django 3.0 on 2019-12-19 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsc_batch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fscbatchturnover',
            name='current_Odate',
            field=models.DateField(verbose_name='Current ODate'),
        ),
    ]