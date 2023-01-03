from django.db import models


class Author(models.Model):
    name_author = models.CharField("Nome Completo", max_length=200)
    email = models.EmailField("Email", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name_author


class Category(models.Model):
    category_name = models.CharField("Categoria", max_length=200)
    description = models.TextField("Descrição")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class Book(models.Model):
    book_title = models.CharField("Título", max_length=200)
    author = models.ManyToManyField(Author)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categories", blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    edition = models.CharField("Edição", max_length=200, blank=True, null=True)
    genre = models.CharField("Gênero textual", max_length=200, blank=True, null=True)
    publishing_company = models.CharField("Editora", max_length=200, blank=True, null=True)
    price = models.DecimalField("Preço", max_digits=7, decimal_places=2,  default=99.99)
    #imagem = models.ImageField(upload_to='livraria/media', blank=True)
    description = models.TextField(blank=True, null=True)
    isbn = models.CharField("ISBN", max_length=13, unique=True, help_text="13 Caracteres <a "
                                                                          "href='https://www.isbn-international.org/content/what-isbn""'>ISBN number</a>")


    class Meta:
        verbose_name_plural = "Books"

    def __str__(self):
        return self.book_title
        if len(self.description > 50):
            return self.description[:50] + "..."




