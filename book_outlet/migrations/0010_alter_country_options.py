# Generated by Django 4.0.5 on 2022-08-07 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0009_country_book_published_countries"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="country",
            options={"verbose_name_plural": "Countries"},
        ),
    ]