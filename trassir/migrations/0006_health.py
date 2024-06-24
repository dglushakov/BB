# Generated by Django 4.2.13 on 2024-06-24 07:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trassir', '0005_rename_uesrname_nvr_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health', models.TextField()),
                ('collected_at', models.DateTimeField(default=datetime.datetime(2024, 6, 24, 10, 22, 12, 183448))),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trassir.nvr')),
            ],
        ),
    ]