# Generated by Django 4.0.1 on 2022-01-31 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_entry_search_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='author',
        ),
    ]