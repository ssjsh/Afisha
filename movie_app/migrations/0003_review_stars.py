# Generated by Django 4.1.7 on 2023-02-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_rename_title_movie_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
