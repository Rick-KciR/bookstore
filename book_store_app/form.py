from django.forms import ModelForm
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["book_title", "author", "description", "price", "category", "isbn"]
