# Generated by Django 2.2.11 on 2020-04-11 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20200410_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlepost',
            old_name='colum',
            new_name='column',
        ),
    ]