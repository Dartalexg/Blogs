# Generated by Django 3.0.5 on 2020-04-10 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='tegs',
            new_name='tag',
        ),
    ]
