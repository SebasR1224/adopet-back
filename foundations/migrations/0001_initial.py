# Generated by Django 4.2.5 on 2023-09-30 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foundation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('introduction', models.TextField(blank=True)),
                ('history', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('webSite', models.URLField(max_length=255)),
                ('nit', models.CharField(max_length=10)),
                ('employeeCount', models.IntegerField(default=0)),
                ('foundationFoundingDate', models.DateField()),
                ('animalsAssistedCount', models.IntegerField(default=0)),
                ('currentAnimalsAssistedCount', models.IntegerField(default=0)),
                ('limitAnimalsAssistedCount', models.IntegerField(default=0)),
                ('foundationRating', models.IntegerField(default=0)),
            ],
        ),
    ]
