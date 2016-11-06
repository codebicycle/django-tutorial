from django.db.models import Count
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, View
from .models import Author, Book
from .forms import ReviewForm

def list_books(request):
    """List the books that have reviews

    """
    books = Book.objects \
            .exclude(date_reviewed__isnull=True) \
            .prefetch_related('authors')

    context = {
        'books': books
    }

    return render(request, 'books/index.html', context)


def review_books(request):
    """List the books that we want to review

    """
    books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')
    context = {
        'books': books,
    }
    return render(request, 'books/list-to-review.html', context)


def review_book(request, pk):
    """Review an individual book

    """
    book = get_object_or_404(Book, pk=pk)
    form = ReviewForm

    context = {
        'book': book,
        'form': form,
    }
    return render(request, 'books/review-book.html', context)


class AuthorList(View):

    def get(self, request):
        authors = Author.objects.annotate(
            published_books=Count('books')
        ). filter(
            published_books__gt=0
        )

        context = {
            'authors': authors,
        }

        return render(request, 'books/authors.html', context)


class BookDetail(DetailView):
    model         = Book
    template_name = 'books/book.html'


class AuthorDetail(DetailView):
    model         = Author
    template_name = 'books/author.html'
