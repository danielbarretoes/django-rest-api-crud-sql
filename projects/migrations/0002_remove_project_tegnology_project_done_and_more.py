# Generated by Django 5.0.1 on 2024-01-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='tegnology',
        ),
        migrations.AddField(
            model_name='project',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]