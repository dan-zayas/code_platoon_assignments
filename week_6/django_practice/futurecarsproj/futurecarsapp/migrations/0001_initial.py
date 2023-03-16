# Generated by Django 4.1.7 on 2023-03-16 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('evil', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('does_fly', models.BooleanField(default=False)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futurecarsapp.make')),
            ],
        ),
    ]
