# Generated by Django 2.1.3 on 2018-12-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0012_auto_20181223_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='members',
            field=models.ManyToManyField(through='profils.UserAchiev', to='profils.Profil'),
        ),
    ]
