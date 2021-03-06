# Generated by Django 2.1.3 on 2018-12-20 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0004_auto_20181217_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercours',
            name='fav',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='members',
            field=models.ManyToManyField(through='profils.UserAchiev', to='profils.Profil'),
        ),
    ]
