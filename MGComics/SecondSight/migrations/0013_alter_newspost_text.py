# Generated by Django 4.0.3 on 2022-05-09 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecondSight', '0012_alter_newspost_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='text',
            field=models.TextField(max_length=5000),
        ),
    ]
