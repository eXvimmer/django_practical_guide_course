# Generated by Django 4.0.5 on 2022-07-24 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0003_book_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="slug",
            field=models.SlugField(blank=True, default=""),
        ),
    ]
