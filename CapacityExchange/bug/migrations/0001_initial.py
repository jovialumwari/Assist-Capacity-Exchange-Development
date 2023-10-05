# Generated by Django 4.2.6 on 2023-10-05 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('bug_type', models.CharField(max_length=100)),
                ('report_date', models.DateField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
