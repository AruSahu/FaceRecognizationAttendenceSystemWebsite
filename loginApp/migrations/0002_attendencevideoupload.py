# Generated by Django 2.2.1 on 2022-01-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendenceVideoUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameTeacher', models.CharField(max_length=255)),
                ('semester', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('videofile', models.FileField(upload_to='')),
            ],
        ),
    ]
