# Generated by Django 4.1.5 on 2024-09-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DetailsApp', '0002_faculty_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semester', models.CharField(max_length=255)),
            ],
        ),
    ]