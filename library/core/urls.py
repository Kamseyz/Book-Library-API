from django.urls import path
from .views import (
    CreateCategoryView,
    UpdateDeleteCategoryView,
    CreateSerializedBook,
    UpdateDeleteSerializedBook,
)

urlpatterns = [
    #create category
    path('category', CreateCategoryView.as_view(), name= 'create_category'),
    #Update/delete category
    path('category/<int:pk>', UpdateDeleteCategoryView.as_view(), name= 'update/delete_category'),
    
    
    # #create book
    path('book', CreateSerializedBook.as_view(), name= 'create_book'),
    #Update/delete book
    path('book/<int:pk>', UpdateDeleteSerializedBook.as_view(), name= 'update/delete_book'),
]
