# Generated by Django 4.0.1 on 2022-01-31 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_remove_entry_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=1),
        ),
    ]