from django.shortcuts import render

def list_books(request):
    return render(request, 'books/index.html')
