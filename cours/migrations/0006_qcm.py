# Generated by Django 2.1.3 on 2018-12-18 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0005_remove_cours_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qcm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]