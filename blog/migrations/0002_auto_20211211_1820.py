# Generated by Django 3.2 on 2021-12-11 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='ceated_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publishd_date',
            new_name='published_date',
        ),
    ]
