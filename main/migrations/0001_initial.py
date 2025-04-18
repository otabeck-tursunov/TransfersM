# Generated by Django 5.2 on 2025-04-05 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='clubs/')),
                ('president', models.CharField(blank=True, max_length=255, null=True)),
                ('coach', models.CharField(blank=True, max_length=255, null=True)),
                ('found_date', models.DateField(blank=True, null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.country')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.club')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.country')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('price_tft', models.FloatField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('new_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_club', to='main.club')),
                ('old_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='old_club', to='main.club')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.player')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.season')),
            ],
        ),
    ]
