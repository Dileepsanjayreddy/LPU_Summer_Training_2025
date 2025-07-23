# CBV
from rest_framework import viewsets
# Create your views here.

from books.models import Book
from books.serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# ======================================================
from django.http import HttpResponse
from rest_framework.decorators import api_view

from books.models import Book
from books.serializers import BookSerializer
from rest_framework.response import Response


# FBV

@api_view(['GET'])
def book_list(request):
    # if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


