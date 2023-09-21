from django.db.models import Prefetch
from .models import Book, Section
from .seriallizers import BookSerializer, SectionSerializer
from rest_framework import generics
from .permissions import (
                         BookAddListPermission, BookUpdatePermission,
                        SectionAddListPermission, SectionUpdatePermission
)


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.prefetch_related(Prefetch(
        'sections',
        queryset=Section.objects.filter(parent=None))).all()
    serializer_class = BookSerializer
    permission_classes = [BookAddListPermission]


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [BookUpdatePermission]


class SectionList(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [SectionAddListPermission]


class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [SectionUpdatePermission]
