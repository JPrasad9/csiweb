# Generated by Django 3.0.1 on 2020-04-21 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200421_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=70)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]