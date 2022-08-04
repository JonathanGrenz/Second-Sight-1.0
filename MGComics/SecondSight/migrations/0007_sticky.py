# Generated by Django 4.0.3 on 2022-04-29 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecondSight', '0006_alter_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sticky',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=25)),
                ('image', models.ImageField(blank=True, default='', upload_to='images/')),
                ('description', models.TextField(blank=True, default='', max_length=900)),
                ('status', models.TextField(blank=True, default='', max_length=900)),
                ('date', models.TextField(blank=True, default='', max_length=900)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
