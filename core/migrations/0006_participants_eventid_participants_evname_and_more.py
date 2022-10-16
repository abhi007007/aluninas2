# Generated by Django 4.0.4 on 2022-10-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='participants',
            name='eventid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='participants',
            name='evname',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='participants',
            name='role',
            field=models.TextField(blank=True, null=True),
        ),
    ]