# Generated by Django 2.1.3 on 2018-12-23 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0011_auto_20181220_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(max_length=60, null=True)),
                ('message', models.CharField(max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img_messages/')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profils.Profil')),
            ],
        ),
        migrations.AlterField(
            model_name='achievement',
            name='members',
            field=models.ManyToManyField(through='profils.UserAchiev', to='profils.Profil'),
        ),
    ]
