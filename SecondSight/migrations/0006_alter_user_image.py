# Generated by Django 4.0.3 on 2022-04-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecondSight', '0005_user_date_user_status_alter_newspost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
    ]