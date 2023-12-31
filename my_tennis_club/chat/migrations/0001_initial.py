# Generated by Django 4.2.7 on 2023-12-22 08:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatLogs',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)])),
                ('user_id', models.IntegerField()),
                ('chat_id', models.IntegerField()),
                ('chat_date', models.DateField()),
                ('chat_title', models.CharField(max_length=255)),
                ('header', models.IntegerField(choices=[(1, 'Header'), (0, 'Content')], default=0)),
                ('role', models.TextField(choices=[('user', 'User'), ('chargpt', 'ChatGPT')])),
                ('prompt', models.TextField()),
            ],
        ),
    ]
