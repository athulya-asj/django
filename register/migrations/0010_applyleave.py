# Generated by Django 3.0 on 2020-01-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_studentattendence'),
    ]

    operations = [
        migrations.CreateModel(
            name='applyleave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('to', models.CharField(max_length=20)),
                ('leavereason', models.CharField(max_length=20)),
                ('fromdate', models.DateField(max_length=10)),
                ('todate', models.DateField(max_length=10)),
            ],
        ),
    ]