# Generated by Django 4.0.2 on 2022-03-24 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='produto',
            field=models.CharField(max_length=100, verbose_name='Produto'),
        ),
    ]
