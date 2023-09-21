from django.urls import path
from .views import BookList, BookDetail, SectionList, SectionDetail

urlpatterns = [
   path('book',BookList.as_view()),
   path('book/<int:pk>',BookDetail.as_view()),
   path('book/section',SectionList.as_view()),
   path('book/section/<int:pk>',SectionDetail.as_view()),
]
