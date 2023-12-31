# Generated by Django 4.2.5 on 2023-09-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=2)),
                ('coatColor', models.CharField(max_length=255)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('breedortype', models.CharField(max_length=50)),
                ('rescueStory', models.TextField()),
                ('rescueDate', models.DateTimeField()),
                ('healtCondition', models.CharField(max_length=255)),
                ('rescuePlace', models.CharField(max_length=255)),
                ('isAdoptable', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]
