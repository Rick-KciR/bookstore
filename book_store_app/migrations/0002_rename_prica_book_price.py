# Generated by Django 4.1.4 on 2023-01-01 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book_store_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="prica",
            new_name="price",
        ),
    ]
