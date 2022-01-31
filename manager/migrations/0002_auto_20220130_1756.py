# Generated by Django 3.2.11 on 2022-01-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'entries'},
        ),
        migrations.AddField(
            model_name='entry',
            name='slug',
            field=models.CharField(default='ed', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
