# Generated by Django 4.0.10 on 2023-10-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=13, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=250)),

            ],
        ),
    ]
