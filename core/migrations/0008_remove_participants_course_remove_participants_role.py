# Generated by Django 4.0.4 on 2022-10-16 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_participants_evname_alter_participants_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participants',
            name='course',
        ),
        migrations.RemoveField(
            model_name='participants',
            name='role',
        ),
    ]