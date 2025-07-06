from rest_framework import generics
from rest_framework import permissions
from .serializer import (
    SerializedCategory, 
    CreateSerializedCategory, 
    UpdateSerializedCategory, 
    CreateSerializedBook,
    UpdateSerializedBook,
    SerializedBook,
)
from rest_framework.pagination import PageNumberPagination
from .models import Book, Category

# Create your views here.


#VIEW TO CREATE AND LIST CATEGORY
class CreateCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateSerializedCategory
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        return Category.objects.filter()

    
# TO UPDATE CATEGORY
class UpdateCategoryView(generics.RetrieveUpdateAPIView):
    queryset = Category
    serializer_class = UpdateSerializedCategory
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Category.objects.filter(user = self.request.user)
    
# TO DELETE CATEORY
class DeleteCategoryView(generics.RetrieveDestroyAPIView):
    serializer_class = SerializedCategory
    queryset = Category
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Category.objects.filter(user = self.request.user)


######################################################################
# TO CREATE AND LIST BOOK
class CreateSerializedBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = CreateSerializedBook
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        return Book.objects.filter()
# TO UPDATE BOOK
class UpdateSerializedBook(generics.RetrieveUpdateAPIView):
    serializer_class = UpdateSerializedBook
    queryset = Book
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Book.objects.filter(posted_by = self.request.user)
    
    
# TO DELETE BOOK RECORDS 

class DeleteSerializedBook(generics.RetrieveDestroyAPIView):
    serializer_class = SerializedBook
    queryset = Book
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Book.objects.filter(posted_by = self.request.user)