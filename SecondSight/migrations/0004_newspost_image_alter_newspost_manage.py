# Generated by Django 4.0.3 on 2022-04-28 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecondSight', '0003_chapter_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='manage',
            field=models.CharField(blank=True, choices=[('s', 'Show'), ('', 'Hide'), ('d', 'DELETE')], default='', max_length=10),
        ),
    ]
