# Generated by Django 4.1.5 on 2024-12-10 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DetailsApp', '0007_alter_studentdatabase_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdatabase',
            name='ATT',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentdatabase',
            name='CLASS',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentdatabase',
            name='SEM',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentdatabase',
            name='SUB',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentdatabase',
            name='USN',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
