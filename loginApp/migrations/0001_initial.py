# Generated by Django 2.2.1 on 2021-12-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginINFO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginID', models.CharField(default='', max_length=60)),
                ('name', models.CharField(default='', max_length=60)),
                ('password', models.CharField(default='', max_length=60)),
                ('phoneNo', models.CharField(default='', max_length=60)),
                ('isAdmin', models.BooleanField(default=False)),
            ],
        ),
    ]
