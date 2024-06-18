# Generated by Django 5.0.4 on 2024-06-18 09:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_category_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserJobInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=150, verbose_name='Job Title')),
                ('job_description', models.TextField(verbose_name='Job Description')),
                ('city', models.CharField(choices=[('TEH', 'Tehran'), ('TEX', 'Texas'), ('MAS', 'Massachusetts'), ('CHI', 'Chicago'), ('SHI', 'Shiraz'), ('ISF', 'Isfahan'), ('PAR', 'Paris'), ('BER', 'Berlin'), ('MUC', 'Munich'), ('ARD', 'Ardabil'), ('TAB', 'Tabriz')], max_length=150, verbose_name='City')),
                ('country', models.CharField(choices=[('IRN', 'Iran'), ('USA', 'United States'), ('GER', 'Germany'), ('FRA', 'France')], max_length=150, verbose_name='Country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
