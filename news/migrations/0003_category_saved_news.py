# Generated by Django 5.2 on 2025-04-09 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='saved_news',
            field=models.ManyToManyField(blank=True, related_name='saved_by', to='news.news'),
        ),
    ]
