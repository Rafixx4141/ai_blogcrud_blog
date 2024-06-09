# Generated by Django 4.0 on 2024-06-09 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_blog_web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='year',
            field=models.PositiveSmallIntegerField(default=2023),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
