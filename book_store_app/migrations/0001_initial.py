# Generated by Django 4.1.4 on 2023-01-01 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name_author",
                    models.CharField(max_length=200, verbose_name="Nome Completo"),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Email"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Authors",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category_name",
                    models.CharField(max_length=200, verbose_name="Categoria"),
                ),
                ("description", models.TextField(verbose_name="Descrição")),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("book_title", models.CharField(max_length=200, verbose_name="Título")),
                ("publication_date", models.DateField(blank=True, null=True)),
                (
                    "edition",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Edição"
                    ),
                ),
                (
                    "genre",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Gênero textual",
                    ),
                ),
                (
                    "publishing_company",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Editora"
                    ),
                ),
                (
                    "prica",
                    models.DecimalField(
                        decimal_places=2,
                        default=99.99,
                        max_digits=7,
                        verbose_name="Preço",
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "isbn",
                    models.CharField(
                        help_text="13 Caracteres <a href='https://www.isbn-international.org/content/what-isbn'>ISBN number</a>",
                        max_length=13,
                        unique=True,
                        verbose_name="ISBN",
                    ),
                ),
                ("author", models.ManyToManyField(to="book_store_app.author")),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="book_store_app.category",
                        verbose_name="Categories",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Books",
            },
        ),
    ]
