# Generated by Django 2.1.7 on 2019-03-28 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corgi_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corgi',
            name='coloring',
            field=models.CharField(choices=[('red', 'Red'), ('rh-tc', 'Red-Headed Tricolor'), ('bh-tc', 'Black-Headed Tricolor'), ('sable', 'Sable'), ('fawn', 'Fawn'), ('other', 'Other')], default='red', max_length=120),
        ),
    ]
