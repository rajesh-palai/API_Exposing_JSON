# Generated by Django 2.2.10 on 2020-07-07 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonpush', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='tz',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
