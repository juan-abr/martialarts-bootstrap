# Generated by Django 4.2.7 on 2024-02-06 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='email',
            field=models.EmailField(default='juantoniorodz@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactpage',
            name='phone',
            field=models.CharField(default='3013058799', max_length=12),
            preserve_default=False,
        ),
    ]
