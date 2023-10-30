# Generated by Django 4.2.6 on 2023-10-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NumberQueryLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queried_number', models.IntegerField(unique=True)),
                ('count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_queried_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]