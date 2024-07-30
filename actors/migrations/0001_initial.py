# Generated by Django 5.0.7 on 2024-07-30 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, choices=[('INDIAN', 'Indiano'), ('USA', 'Estados Unidos'), ('BRAZIL', 'Brasil')], max_length=100, null=True)),
            ],
        ),
    ]
