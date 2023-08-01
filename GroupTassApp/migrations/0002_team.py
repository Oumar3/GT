# Generated by Django 4.0 on 2023-07-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroupTassApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('nom', models.CharField(max_length=150)),
                ('post', models.CharField(max_length=100)),
                ('twitter', models.URLField(blank=True, default='#', null=True)),
                ('facebook', models.URLField(blank=True, default='#', null=True)),
                ('instagram', models.URLField(blank=True, default='#', null=True)),
                ('linkedin', models.URLField(blank=True, default='#', null=True)),
            ],
        ),
    ]
