# Generated by Django 3.2 on 2022-03-29 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='full_name',
        ),
    ]
