# Generated by Django 4.0 on 2023-07-31 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroupTassApp', '0003_motdumembre'),
    ]

    operations = [
        migrations.AddField(
            model_name='motdumembre',
            name='mot',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
