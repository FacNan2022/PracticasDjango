# Generated by Django 4.2.1 on 2023-05-30 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='signature',
            field=models.CharField(default='firma', max_length=100),
        ),
    ]