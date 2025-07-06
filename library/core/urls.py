from django.urls import path
from .views import (
    CreateCategoryView,
    UpdateCategoryView,
    DeleteCategoryView,
    CreateSerializedBook,
    UpdateSerializedBook,
    DeleteSerializedBook,
)

urlpatterns = [
    #create category
    path('create_category/', CreateCategoryView.as_view(), name= 'create_category'),
    #Update category
    path('update/<int:pk>/category/', UpdateCategoryView.as_view(), name= 'update_category'),
    # #Delete category
    path('delete/<int:pk>/category/', DeleteCategoryView.as_view(), name= 'delete_category'),
    # #create book
    path('create_book/', CreateSerializedBook.as_view(), name= 'create_book'),
    #Update book
    path('update/<int:pk>/book/', UpdateSerializedBook.as_view(), name= 'update_book'),
    #Update category
    path('delete/<int:pk>/book/', DeleteSerializedBook.as_view(), name= 'delete_book'),

]
