# Generated by Django 2.1.3 on 2018-12-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0007_auto_20181220_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='prerequis',
            field=models.ManyToManyField(to='cours.Cours'),
        ),
    ]
