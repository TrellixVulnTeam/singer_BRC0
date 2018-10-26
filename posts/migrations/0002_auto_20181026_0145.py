# Generated by Django 2.1.2 on 2018-10-26 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('I', 'INFRASTRUCTURA'), ('E', 'EDUCACION'), ('S', 'SALUD'), ('T', 'TRANSPORTE'), ('B', 'BIENESTAR CIUDADANO'), ('O', 'OTRA')], default='O', max_length=1),
        ),
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='N/A', max_length=255),
        ),
    ]
